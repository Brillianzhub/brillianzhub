import json
import os

directory = 'D:/DOCS/Web Developement/Codecademy/projects/brillianzhub/src'
filename = 'verses_kjv.json'

file_path = os.path.join(directory, filename)

with open(file_path, 'r') as file:
    data = json.load(file)


def remove_trailing_whitespace(text):
    return text.strip()


for item in data:
    if 'text' in item:
        item['text'] = remove_trailing_whitespace(item['text'])

output_filename = 'cleaned_data_no_whitespace.json'
output_file_path = os.path.join(directory, output_filename)
with open(output_file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Trailing whitespace removed and cleaned data saved to", output_file_path)
