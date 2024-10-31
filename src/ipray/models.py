from django.db import models
from django.conf import settings
from django.utils.text import Truncator, slugify
from django.contrib.auth.hashers import make_password, check_password



class IPrayUser(models.Model):
    google_id = models.CharField(max_length=100, unique=True, blank=True, null=True)  
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    profile_picture = models.URLField(blank=True, null=True)
    auth_provider = models.CharField(max_length=50, default='email')  
    password = models.CharField(max_length=255, blank=True, null=True) 

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class PrayerPoint(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='prayer_points', on_delete=models.CASCADE)
    prayer_long = models.TextField(null=True, blank=True)
    text = models.TextField()
    category = models.ForeignKey(
        Category, related_name='prayer_category', on_delete=models.CASCADE)
    bible_quotation = models.TextField(null=True, blank=True)
    bible_verse = models.TextField()

    def __str__(self):
        truncated_text = Truncator(self.text).words(10, truncate='...', html=True)
        return f"{self.category.title} {self.bible_quotation} - {truncated_text}"



class Version(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.abbreviation


class Book(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name='book_category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.category}"

    def get_next_book(self):
        next_book = Book.objects.filter(id__gt=self.id).order_by('id').first()
        return next_book

    def get_previous_book(self):
        previous_book = Book.objects.filter(
            id__lt=self.id).order_by('-id').first()
        return previous_book


class Chapter(models.Model):
    book = models.ForeignKey(
        Book, related_name='chapters', on_delete=models.CASCADE)
    number = models.IntegerField()

    class Meta:
        unique_together = ('book', 'number')
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"
        ordering = ['book', 'number']

    def __str__(self):
        return f"{self.book.name} {self.number}"

    def get_next_chapter(self):
        next_chapter = Chapter.objects.filter(book=self.book, number=self.number + 1).first()
        return next_chapter

    def get_previous_chapter(self):
        previous_chapter = Chapter.objects.filter(book=self.book, number=self.number - 1).first()
        return previous_chapter


class Verse(models.Model):
    chapter = models.ForeignKey(
        Chapter, related_name='verses', on_delete=models.CASCADE)
    verse = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('chapter', 'verse')

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.verse}"



class Subscriber(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Promise(models.Model):
    book = models.CharField(max_length=100)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    text = models.TextField()
    version = models.ForeignKey(Version, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} {self.chapter}:{self.verse} ({self.version.abbreviation})"


# class BookNIV(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name}"


# class ChapterNIV(models.Model):
#     book = models.ForeignKey(
#         BookNIV, related_name='chapters_niv', on_delete=models.CASCADE)
#     number = models.IntegerField()

#     class Meta:
#         unique_together = ('book', 'number')
#         verbose_name = "Chapter"
#         verbose_name_plural = "Chapters amp"
#         ordering = ['book', 'number']


class VerseKJV(models.Model):
    chapter = models.ForeignKey(
        Chapter, related_name='verses_kjv', on_delete=models.CASCADE)
    verse = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('chapter', 'verse')

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.verse}"

    def next_verse(self):
        next_verse = VerseKJV.objects.filter(
            chapter=self.chapter, verse__gt=self.verse).order_by('verse').first()

        if next_verse:
            return next_verse

        next_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__gt=self.chapter.number).order_by('number').first()

        if next_chapter:
            return VerseKJV.objects.filter(chapter=next_chapter).order_by('verse').first()

        return None

    def previous_verse(self):
        previous_verse = VerseKJV.objects.filter(
            chapter=self.chapter, verse__lt=self.verse).order_by('-verse').first()

        if previous_verse:
            return previous_verse

        previous_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__lt=self.chapter.number).order_by('-number').first()

        if previous_chapter:
            return VerseKJV.objects.filter(chapter=previous_chapter).order_by('-verse').first()

        return None


class VerseAMP(models.Model):
    chapter = models.ForeignKey(
        Chapter, related_name='verses_amp', on_delete=models.CASCADE)
    verse = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('chapter', 'verse')

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.verse}"


    def next_verse(self):
        next_verse = VerseAMP.objects.filter(
            chapter=self.chapter, verse__gt=self.verse).order_by('verse').first()

        if next_verse:
            return next_verse

        next_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__gt=self.chapter.number).order_by('number').first()

        if next_chapter:
            return VerseAMP.objects.filter(chapter=next_chapter).order_by('verse').first()

        return None

    def previous_verse(self):
        previous_verse = VerseAMP.objects.filter(
            chapter=self.chapter, verse__lt=self.verse).order_by('-verse').first()

        if previous_verse:
            return previous_verse

        previous_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__lt=self.chapter.number).order_by('-number').first()

        if previous_chapter:
            return VerseAMP.objects.filter(chapter=previous_chapter).order_by('-verse').first()

        return None



class VerseASV(models.Model):
    chapter = models.ForeignKey(
        Chapter, related_name='verses_asv', on_delete=models.CASCADE)
    verse = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('chapter', 'verse')

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.verse}"

    def next_verse(self):
        next_verse = VerseASV.objects.filter(
            chapter=self.chapter, verse__gt=self.verse).order_by('verse').first()

        if next_verse:
            return next_verse

        next_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__gt=self.chapter.number).order_by('number').first()

        if next_chapter:
            return VerseASV.objects.filter(chapter=next_chapter).order_by('verse').first()

        return None

    def previous_verse(self):
        previous_verse = VerseASV.objects.filter(
            chapter=self.chapter, verse__lt=self.verse).order_by('-verse').first()

        if previous_verse:
            return previous_verse

        previous_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__lt=self.chapter.number).order_by('-number').first()

        if previous_chapter:
            return VerseASV.objects.filter(chapter=previous_chapter).order_by('-verse').first()

        return None



class VerseNIV(models.Model):
    chapter = models.ForeignKey(
        Chapter, related_name='verses_niv', on_delete=models.CASCADE)
    verse = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('chapter', 'verse')

    def __str__(self):
        return f"{self.chapter.book.name} {self.chapter.number}:{self.verse}"

    def next_verse(self):
        next_verse = VerseNIV.objects.filter(
            chapter=self.chapter, verse__gt=self.verse).order_by('verse').first()

        if next_verse:
            return next_verse

        next_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__gt=self.chapter.number).order_by('number').first()

        if next_chapter:
            return VerseNIV.objects.filter(chapter=next_chapter).order_by('verse').first()

        return None

    def previous_verse(self):
        previous_verse = VerseNIV.objects.filter(
            chapter=self.chapter, verse__lt=self.verse).order_by('-verse').first()

        if previous_verse:
            return previous_verse

        previous_chapter = Chapter.objects.filter(
            book=self.chapter.book, number__lt=self.chapter.number).order_by('-number').first()

        if previous_chapter:
            return VerseNIV.objects.filter(chapter=previous_chapter).order_by('-verse').first()

        return None



class KoinoniaMessage(models.Model):
    # Fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    date = models.DateField()  # For a true date field
    read_time = models.IntegerField(help_text="Reading time in minutes")
    youtube_link = models.URLField(max_length=500, blank=True, null=True)
    download_link = models.CharField(max_length=500, blank=True, null=True)
    download_audio_link = models.CharField(max_length=500, blank=True, null=True)  # New field for audio download

    # Generate slug automatically when saving
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(KoinoniaMessage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title











