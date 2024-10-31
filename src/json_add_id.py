import os
import json

# Define the directory and filename
directory = 'D:/DOCS/Web Developement/Codecademy/projects/brillianzhub/src'
filename = 'kjv_json_restructured.json'

# Combine directory and filename to create the full path for input and output
input_file = os.path.join(directory, filename)
output_file = os.path.join(directory, 'verses_with_ids_and_chapter_numbers_niv.json')

def add_ids_and_category_to_bible_data(bible_data):
    # Initialize counters for IDs
    book_counter = 1
    chapter_counter = 1
    verse_counter = 1

    # Iterate over books
    for book in bible_data:
        # Add book_id
        book['book_id'] = book_counter

        # Add category based on book_id
        if 1 <= book_counter <= 39:
            book['category'] = 'Old Testament'
        elif 40 <= book_counter <= 66:
            book['category'] = 'New Testament'

        # Iterate over chapters
        new_chapters = {}
        for chapter_number, verses in book['chapters'].items():
            # Create a new chapter structure with continuous chapter_id and add chapter_number
            new_chapters[chapter_number] = {
                'chapter_id': chapter_counter,
                'chapter_number': chapter_number,  # Preserve the original chapter_number
                'verses': []
            }

            # Iterate over verses
            for verse in verses:
                # Add continuous verse_id
                verse_with_id = {
                    'verse_id': verse_counter,
                    'verse_number': verse['verse_number'],
                    'text': verse['text']
                }

                # Add the updated verse to the chapter's verses list
                new_chapters[chapter_number]['verses'].append(verse_with_id)

                verse_counter += 1

            chapter_counter += 1

        # Replace the old chapters with the new structure
        book['chapters'] = new_chapters
        book_counter += 1

    return bible_data

# Read the original JSON data
with open(input_file, 'r') as f:
    bible_data = json.load(f)

# Add IDs and categories to the Bible data
bible_data_with_ids_and_chapter_numbers = add_ids_and_category_to_bible_data(bible_data)

# Write the updated data to a new file
with open(output_file, 'w') as f:
    json.dump(bible_data_with_ids_and_chapter_numbers, f, indent=4)

print(f"Updated Bible data with IDs, categories, and chapter numbers has been saved to {output_file}")
