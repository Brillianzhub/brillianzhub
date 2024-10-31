import json

# Paths to input and output files
input_file_path = 'D:/DOCS/Web Developement/Codecademy/projects/brillianzhub/src/tt_data.json'
output_file_path = 'D:/DOCS/Web Developement/Codecademy/projects/brillianzhub/src/transformed_verses.json'


def transform_bible_data(data):
    transformed_data = []
    verse_id_counter = 1
    chapter_id_counter = 1

    for book in data:
        book_info = {
            "id": book["book_id"],
            "name": book["book_name"],
            "category": book["category"]
        }

        for chapter_number, chapter in book["chapters"].items():
            transformed_chapter = {
                "id": chapter_id_counter,
                "chapter_number": int(chapter_number),
                "book": [book_info],
                "verses": []
            }

            for verse in chapter["verses"]:
                transformed_verse = {
                    "verse_id": verse_id_counter,
                    "verse_number": int(verse["verse_number"]),
                    "text": verse["text"]
                }
                transformed_chapter["verses"].append(transformed_verse)
                verse_id_counter += 1

            transformed_data.append(transformed_chapter)
            chapter_id_counter += 1

    return transformed_data


# Read the original JSON data
with open(input_file_path, 'r', encoding='utf-8') as f:
    original_data = json.load(f)

# Transform the data
transformed_data = transform_bible_data(original_data)

# Save the transformed data to a new JSON file with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(transformed_data, f, ensure_ascii=False, indent=4)

print(f'Transformed data saved to {output_file_path}')


