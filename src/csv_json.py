import csv
import json

# File paths
csv_file_path = 'D:/DOCS/Web Developement/Codecademy/projects/brillianzhub/src/NIV.csv'  
json_file_path = 'niv_data.json' 

def get_category(book_id):
    return "Old Testament" if 1 <= book_id <= 39 else "New Testament"

# Read the CSV and process the data
def csv_to_json(csv_file):
    bible_data = []
    book_dict = {}
    book_id_counter = 1
    chapter_id_counter = 1
    verse_id_counter = 1

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            book_name = row['book_name']
            chapter_number = row['chapter_number']
            verse_number = row['verse_number']
            text = row['text']

            # Check if the book already exists in the data
            if book_name not in book_dict:
                # Assign a new book_id and create a new book entry
                book_id = book_id_counter
                book_dict[book_name] = {
                    "book_name": book_name,
                    "book_id": book_id,
                    "category": get_category(book_id),
                    "chapters": {}
                }
                book_id_counter += 1
            
            # Get the current book
            book = book_dict[book_name]

            # Check if the chapter already exists in the book
            if chapter_number not in book["chapters"]:
                # Create a new chapter entry
                book["chapters"][chapter_number] = {
                    "chapter_id": chapter_id_counter,
                    "chapter_number": chapter_number,
                    "verses": []
                }
                chapter_id_counter += 1

            # Get the current chapter
            chapter = book["chapters"][chapter_number]

            # Add the verse to the chapter
            chapter["verses"].append({
                "verse_id": verse_id_counter,
                "verse_number": verse_number,
                "text": text
            })
            verse_id_counter += 1

    # Convert the dictionary to a list of books
    bible_data = list(book_dict.values())
    return bible_data

# Convert CSV to JSON and save to file
bible_data = csv_to_json(csv_file_path)

# Save the transformed data to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(bible_data, json_file, ensure_ascii=False, indent=4)

print(f"JSON file saved to {json_file_path}")
