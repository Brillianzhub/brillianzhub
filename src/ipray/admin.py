from django.contrib import admin
from . models import Category, PrayerPoint, Promise, Book, Chapter, Verse, VerseASV, VerseKJV, VerseAMP, VerseNIV, IPrayUser, Version, KoinoniaMessage, Subscriber
# Register your models here.



class KoinoniaMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'read_time', 'slug')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(KoinoniaMessage, KoinoniaMessageAdmin)



class VerseKJVAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    search_fields = ['text']



class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(IPrayUser)
admin.site.register(Category)
admin.site.register(PrayerPoint)
admin.site.register(Promise)
admin.site.register(Version)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Verse)
admin.site.register(VerseASV)
admin.site.register(VerseKJV, VerseKJVAdmin)
admin.site.register(VerseAMP)
admin.site.register(VerseNIV)