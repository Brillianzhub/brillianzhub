from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils import timezone


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
