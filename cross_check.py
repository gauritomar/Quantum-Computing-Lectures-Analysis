import json

# Read the content of the JSON file
with open("cleaned_topics.json", "r") as file:
    string_list = json.load(file)

# Convert each string element to JSON object
json_objects = [json.loads(string) for string in string_list]

with open("cleaned_jsons.json", "w") as file:
    json.dump(json_objects, file, indent=4)
