# myapp/views.py

from .serializers import CategorySerializer, PrayerPointSerializer, BookSerializer, ChapterSerializer, VerseSerializer, VerseASVSerializer, VerseAMPSerializer, VerseNIVSerializer, PromiseSerializer
from .models import Book, Category, Chapter, VerseKJV, PrayerPoint, VerseASV, VerseAMP, VerseNIV, IPrayUser, Promise, Subscriber
from rest_framework import viewsets
from notifications.models import Device
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
import json



@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            auth_provider = data.get('auth_provider', 'email')

            if not name or not email or not password:
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            # Check if user already exists
            if IPrayUser.objects.filter(email=email).exists():
                return JsonResponse({'error': 'User with this email already exists.'}, status=400)

            # Create new user
            user = IPrayUser(
                name=name,
                email=email,
                auth_provider=auth_provider
            )

            # Hash password if the user signs up via email/password
            if auth_provider == 'email':
                user.password = make_password(password)

            user.save()

            return JsonResponse({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'profile_picture': user.profile_picture
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Failed to sign up: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


@csrf_exempt
def google_sign_in(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            google_id = data.get('google_id')
            email = data.get('email')
            name = data.get('name')
            profile_picture = data.get('profile_picture')
            device_token = data.get('device_token')

            if not google_id or not email or not name:
                return JsonResponse({'error': 'Missing required Google user data.'}, status=400)

            # Check if user already exists
            user = IPrayUser.objects.filter(email=email).first()

            if user:
                # Update existing user’s Google ID and profile picture if they exist but don't have it set
                if not user.google_id:
                    user.google_id = google_id
                if not user.profile_picture:
                    user.profile_picture = profile_picture
                user.save()

            else:
                # Create a new user
                user = IPrayUser.objects.create(
                    google_id=google_id,
                    email=email,
                    name=name,
                    profile_picture=profile_picture,
                    auth_provider='google'
                )

            if device_token:
                Device.objects.update_or_create(
                    token = device_token,
                    defaults = {'user': user}
                )

            return JsonResponse({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'profile_picture': user.profile_picture
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            device_token = data.get('device_token')  # Device token from frontend

            try:
                user = IPrayUser.objects.get(email=email, auth_provider='email')
            except IPrayUser.DoesNotExist:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)

            if user.check_password(password):
                # Associate the device token with the user
                if device_token:
                    # Update or create a device entry
                    device, created = Device.objects.update_or_create(
                        token=device_token,
                        defaults={'user': user}
                    )

                return JsonResponse({
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'auth_provider': user.auth_provider,
                    'profile_picture': user.profile_picture,
                }, status=200)
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=200)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PrayerPointViewSet(viewsets.ModelViewSet):
    queryset = PrayerPoint.objects.all()
    serializer_class = PrayerPointSerializer

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category_title = request.query_params.get('category', None)

        if category_title:
            try:
                category = Category.objects.get(title=category_title)
                prayer_points = PrayerPoint.objects.filter(category=category)
                serializer = PrayerPointSerializer(prayer_points, many=True)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({'error': 'Category not found'}, status=404)
        else:
            return Response({'error': 'Category title is required'}, status=400)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        queryset = Chapter.objects.all()
        book_id = self.request.query_params.get('book_id')
        if book_id:
            queryset = queryset.filter(book__id=book_id)
        return queryset


class PromiseViewSet(viewsets.ModelViewSet):
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer

class VerseViewSet(viewsets.ModelViewSet):
    queryset = VerseKJV.objects.all()
    serializer_class = VerseSerializer

    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        queryset = self.queryset
        if chapter_id:
            queryset = queryset.filter(chapter_id=chapter_id)
        return queryset


class VerseASVViewSet(viewsets.ModelViewSet):
    queryset = VerseASV.objects.all()
    serializer_class = VerseASVSerializer

    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        queryset = self.queryset
        if chapter_id:
            queryset = queryset.filter(chapter_id=chapter_id)
        return queryset


class VerseAMPViewSet(viewsets.ModelViewSet):
    queryset = VerseAMP.objects.all()
    serializer_class = VerseAMPSerializer

    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        queryset = self.queryset
        if chapter_id:
            queryset = queryset.filter(chapter_id=chapter_id)
        return queryset


class VerseNIVViewSet(viewsets.ModelViewSet):
    queryset = VerseNIV.objects.all()
    serializer_class = VerseNIVSerializer

    def get_queryset(self):
        chapter_id = self.request.query_params.get('chapter_id')
        queryset = self.queryset
        if chapter_id:
            queryset = queryset.filter(chapter_id=chapter_id)
        return queryset




@csrf_exempt
def subscribe(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({"message": "Invalid email address."}, status=400)

            # Check if the email is already subscribed
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({"message": "This email is already subscribed."}, status=400)

            # Save new subscriber
            Subscriber.objects.create(email=email)
            return JsonResponse({"message": "Subscription successful!"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid data format."}, status=400)
        except Exception as e:
            return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)

    return JsonResponse({"message": "Only POST requests are allowed."}, status=405)

