# myapp/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PrayerPointViewSet, BookViewSet, ChapterViewSet, VerseViewSet, VerseASVViewSet, VerseAMPViewSet, VerseNIVViewSet, PromiseViewSet
from . import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'prayerpoints', PrayerPointViewSet)
router.register(r'promises', PromiseViewSet)
router.register(r'bible_books', BookViewSet)
router.register(r'bible_chapters', ChapterViewSet)
router.register(r'bible_verses_kjv', VerseViewSet)

router.register(r'bible_verses_asv', VerseASVViewSet)

router.register(r'bible_verses_amp', VerseAMPViewSet)

router.register(r'bible_verses_niv', VerseNIVViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.register_user, name='register_user'),
    path('google-signin/', views.google_sign_in, name='google_sign_in'),
    path('logout/', views.logout_view, name='logout'),
    path('signin/', views.login_view, name='signin'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
