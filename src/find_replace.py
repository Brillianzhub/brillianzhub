import json
import os
from collections import defaultdict


def restructure_json(input_file, output_file):
    # Open and load the JSON file
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    # Create a nested structure based on book_name
    books = defaultdict(
        lambda: {"book_name": "", "chapters": defaultdict(list)})

    for entry in data:
        book_name = entry["book_name"]
        chapter_number = entry["chapter_number"]
        verse_number = entry["verse_number"]
        text = entry["text"]

        if books[book_name]["book_name"] == "":
            books[book_name]["book_name"] = book_name

        # Append verses to the corresponding chapter
        books[book_name]["chapters"][chapter_number].append({
            "verse_number": verse_number,
            "text": text
        })

    # Convert defaultdict to normal dict
    result = []
    for book, content in books.items():
        content["chapters"] = dict(content["chapters"])
        result.append(content)

    # Save the restructured JSON to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, indent=4)


if __name__ == "__main__":
    # Path to the directory containing your JSON file
    directory = 'D:/DOCS/Web Developement/Codecademy/projects/brillianzhub/src'
    filename = 'kjv_json.json'

    input_file = os.path.join(directory, filename)

    # Specify the output JSON file path
    output_file = os.path.join(directory, 'kjv_json_restructured.json')

    restructure_json(input_file, output_file)
    print(
        f"JSON file '{input_file}' has been restructured and saved to '{output_file}'")
