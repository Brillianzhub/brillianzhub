# Generated by Django 3.2.13 on 2024-10-31 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='ipray.book')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
                'ordering': ['book', 'number'],
                'unique_together': {('book', 'number')},
            },
        ),
        migrations.CreateModel(
            name='IPrayUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('profile_picture', models.URLField(blank=True, null=True)),
                ('auth_provider', models.CharField(default='email', max_length=50)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KoinoniaMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('read_time', models.IntegerField(help_text='Reading time in minutes')),
                ('youtube_link', models.URLField(blank=True, max_length=500, null=True)),
                ('download_link', models.CharField(blank=True, max_length=500, null=True)),
                ('download_audio_link', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Promise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=100)),
                ('chapter', models.IntegerField()),
                ('verse', models.IntegerField()),
                ('text', models.TextField()),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipray.version')),
            ],
        ),
        migrations.CreateModel(
            name='PrayerPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prayer_long', models.TextField(blank=True, null=True)),
                ('text', models.TextField()),
                ('bible_quotation', models.TextField(blank=True, null=True)),
                ('bible_verse', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prayer_category', to='ipray.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prayer_points', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='ipray.category'),
        ),
        migrations.CreateModel(
            name='VerseNIV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.IntegerField()),
                ('text', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses_niv', to='ipray.chapter')),
            ],
            options={
                'unique_together': {('chapter', 'verse')},
            },
        ),
        migrations.CreateModel(
            name='VerseKJV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.IntegerField()),
                ('text', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses_kjv', to='ipray.chapter')),
            ],
            options={
                'unique_together': {('chapter', 'verse')},
            },
        ),
        migrations.CreateModel(
            name='VerseASV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.IntegerField()),
                ('text', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses_asv', to='ipray.chapter')),
            ],
            options={
                'unique_together': {('chapter', 'verse')},
            },
        ),
        migrations.CreateModel(
            name='VerseAMP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.IntegerField()),
                ('text', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses_amp', to='ipray.chapter')),
            ],
            options={
                'unique_together': {('chapter', 'verse')},
            },
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verse', models.IntegerField()),
                ('text', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses', to='ipray.chapter')),
            ],
            options={
                'unique_together': {('chapter', 'verse')},
            },
        ),
    ]
