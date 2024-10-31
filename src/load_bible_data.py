import csv
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brillianzhub.settings')
django.setup()

from ipray.models import BookKJV, ChapterKJV, VerseKJV

def load_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book_name = row['book_name']
            chapter_number = int(row['chapter_number'])
            verse_number = int(row['verse_number'])
            verse_text = row['text']

            # Get or create the book
            name, created = BookKJV.objects.get_or_create(name=book_name)

            # Get or create the chapter
            number, created = ChapterKJV.objects.get_or_create(
                book=name, number=chapter_number)

            # Check if the verse already exists
            verse, created = VerseKJV.objects.get_or_create(
                chapter=number,
                verse=verse_number,
                defaults={'text': verse_text}
            )
            # Update the verse text if it already exists
            if not created:
                verse.text = verse_text
                verse.save()


if __name__ == "__main__":
    load_data('./bible.csv')
