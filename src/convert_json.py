import json
import os

# Path to the directory containing your JSON file
directory = 'D:/DOCS/Web Developement/Codecademy/projects/brillianzhub/src'
filename = 'verses_niv.json'

# Construct the full file path
file_path = os.path.join(directory, filename)

# Load the JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Initialize an empty list to hold cleaned data
cleaned_data = []

# Iterate through the loaded data and transform it
for item in data:
    cleaned_item = {
        "id": item["pk"],
        "chapter": item["fields"]["chapter"],
        "verse": item["fields"]["verse"],
        "text": item["fields"]["text"]
    }
    cleaned_data.append(cleaned_item)

# Optionally, convert the cleaned data to JSON format
cleaned_data_json = json.dumps(cleaned_data, indent=4)

# Print or save the cleaned data
print(cleaned_data_json)

# If you want to save it to a new file:
output_filename = 'cleaned_data.json'
output_file_path = os.path.join(directory, output_filename)
with open(output_file_path, 'w') as f:
    f.write(cleaned_data_json)
