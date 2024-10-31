from rest_framework import serializers
from .models import Category, PrayerPoint, Book, Chapter, VerseKJV, VerseASV, VerseAMP, VerseNIV, Promise, Version
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PrayerPointSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = PrayerPoint
        fields = '__all__'


class SimplifiedBookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ('id', 'name', 'category')


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    next_book = serializers.SerializerMethodField()
    previous_book = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'category', 'next_book', 'previous_book')

    def get_next_book(self, obj):
        next_book = obj.get_next_book()
        return SimplifiedBookSerializer(next_book).data if next_book else None

    def get_previous_book(self, obj):
        previous_book = obj.get_previous_book()
        return SimplifiedBookSerializer(previous_book).data if previous_book else None


class ChapterSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    next_chapter = serializers.SerializerMethodField()
    previous_chapter = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = ('id', 'book', 'number', 'next_chapter', 'previous_chapter',)

    def get_next_chapter(self, obj):
        next_chapter = obj.get_next_chapter()
        if next_chapter:
            return {
                'id': next_chapter.id,
                'book': {
                    'id': next_chapter.book.id,
                    'name': next_chapter.book.name
                },
                'number': next_chapter.number
            }
        return None

    def get_previous_chapter(self, obj):
        previous_chapter = obj.get_previous_chapter()
        if previous_chapter:
            return {
                'id': previous_chapter.id,
                'book': {
                    'id': previous_chapter.book.id,
                    'name': previous_chapter.book.name
                },
                'number': previous_chapter.number
            }
        return None


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ['id', 'name', 'abbreviation']


class PromiseSerializer(serializers.ModelSerializer):

    version = VersionSerializer()

    class Meta:
        model = Promise
        fields = ['id', 'book', 'chapter', 'verse', 'text', 'version']


# class VerseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VerseKJV
#         fields = ['id', 'verse', 'text', 'chapter']

#     def __init__(self, *args, **kwargs):
#         self.chapter_id = kwargs.pop('chapter_id', None)
#         super().__init__(*args, **kwargs)

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         if self.chapter_id is not None and instance.chapter_id != self.chapter_id:
#             return None
#         return data

class VerseSerializer(serializers.ModelSerializer):
    next_verse = serializers.SerializerMethodField()
    previous_verse = serializers.SerializerMethodField()

    class Meta:
        model = VerseKJV
        fields = ['id', 'verse', 'text', 'chapter', 'next_verse', 'previous_verse']

    def __init__(self, *args, **kwargs):
        self.chapter_id = kwargs.pop('chapter_id', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        # Call the parent method to get the default representation
        data = super().to_representation(instance)

        # Check if a chapter_id was provided and if the instance belongs to the chapter
        if self.chapter_id is not None and instance.chapter_id != self.chapter_id:
            return None

        return data

    # Method to retrieve the next verse
    def get_next_verse(self, instance):
        next_verse = instance.next_verse()  # Call the next_verse method on the model
        if next_verse:
            return {
                'id': next_verse.id,
                'verse': next_verse.verse,
                'text': next_verse.text,
                'chapter': next_verse.chapter.number,
                'book': next_verse.chapter.book.name
            }
        return None

    # Method to retrieve the previous verse
    def get_previous_verse(self, instance):
        previous_verse = instance.previous_verse()  # Call the previous_verse method on the model
        if previous_verse:
            return {
                'id': previous_verse.id,
                'verse': previous_verse.verse,
                'text': previous_verse.text,
                'chapter': previous_verse.chapter.number,
                'book': previous_verse.chapter.book.name
            }
        return None



class VerseASVSerializer(serializers.ModelSerializer):
    next_verse = serializers.SerializerMethodField()
    previous_verse = serializers.SerializerMethodField()

    class Meta:
        model = VerseASV
        fields = ['id', 'verse', 'text', 'chapter', 'next_verse', 'previous_verse']

    def __init__(self, *args, **kwargs):
        self.chapter_id = kwargs.pop('chapter_id', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.chapter_id is not None and instance.chapter_is != self.chapter_id:
            return None
        return data

    # Method to retrieve the next verse
    def get_next_verse(self, instance):
        next_verse = instance.next_verse()  # Call the next_verse method on the model
        if next_verse:
            return {
                'id': next_verse.id,
                'verse': next_verse.verse,
                'text': next_verse.text,
                'chapter': next_verse.chapter.number,
                'book': next_verse.chapter.book.name
            }
        return None

    # Method to retrieve the previous verse
    def get_previous_verse(self, instance):
        previous_verse = instance.previous_verse()  # Call the previous_verse method on the model
        if previous_verse:
            return {
                'id': previous_verse.id,
                'verse': previous_verse.verse,
                'text': previous_verse.text,
                'chapter': previous_verse.chapter.number,
                'book': previous_verse.chapter.book.name
            }
        return None


class VerseAMPSerializer(serializers.ModelSerializer):
    next_verse = serializers.SerializerMethodField()
    previous_verse = serializers.SerializerMethodField()

    class Meta:
        model = VerseAMP
        fields = ['id', 'verse', 'text', 'chapter', 'next_verse', 'previous_verse']

    def __init__(self, *args, **kwargs):
        self.chapter_id = kwargs.pop('chapter_id', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.chapter_id is not None and instance.chapter_is != self.chapter_id:
            return None
        return data

    # Method to retrieve the next verse
    def get_next_verse(self, instance):
        next_verse = instance.next_verse()  # Call the next_verse method on the model
        if next_verse:
            return {
                'id': next_verse.id,
                'verse': next_verse.verse,
                'text': next_verse.text,
                'chapter': next_verse.chapter.number,
                'book': next_verse.chapter.book.name
            }
        return None

    # Method to retrieve the previous verse
    def get_previous_verse(self, instance):
        previous_verse = instance.previous_verse()  # Call the previous_verse method on the model
        if previous_verse:
            return {
                'id': previous_verse.id,
                'verse': previous_verse.verse,
                'text': previous_verse.text,
                'chapter': previous_verse.chapter.number,
                'book': previous_verse.chapter.book.name
            }
        return None



class VerseNIVSerializer(serializers.ModelSerializer):
    next_verse = serializers.SerializerMethodField()
    previous_verse = serializers.SerializerMethodField()

    class Meta:
        model = VerseNIV
        fields = ['id', 'verse', 'text', 'chapter', 'next_verse', 'previous_verse']

    def __init__(self, *args, **kwargs):
        self.chapter_id = kwargs.pop('chapter_id', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.chapter_id is not None and instance.chapter_is != self.chapter_id:
            return None
        return data

    # Method to retrieve the next verse
    def get_next_verse(self, instance):
        next_verse = instance.next_verse()  # Call the next_verse method on the model
        if next_verse:
            return {
                'id': next_verse.id,
                'verse': next_verse.verse,
                'text': next_verse.text,
                'chapter': next_verse.chapter.number,
                'book': next_verse.chapter.book.name
            }
        return None

    # Method to retrieve the previous verse
    def get_previous_verse(self, instance):
        previous_verse = instance.previous_verse()  # Call the previous_verse method on the model
        if previous_verse:
            return {
                'id': previous_verse.id,
                'verse': previous_verse.verse,
                'text': previous_verse.text,
                'chapter': previous_verse.chapter.number,
                'book': previous_verse.chapter.book.name
            }
        return None





















