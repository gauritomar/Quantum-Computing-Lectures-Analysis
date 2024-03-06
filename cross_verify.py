import json

# Load data from cleaned_jsons.json
with open("cleaned_jsons.json", "r") as file:
    cleaned_jsons = json.load(file)

# Load data from summarised_topics.json
with open("summarised_topics.json", "r") as file:
    summarised_topics = json.load(file)

# Extract titles from each JSON object
cleaned_titles = {obj["title"].replace('.mp4', '').replace('.vtt', '') for obj in cleaned_jsons}
summarised_titles = {lecture["title"].replace('.mp4', '').replace('.vtt', '') for lecture in summarised_topics}

# Find titles that are not common
titles_not_in_cleaned = summarised_titles - cleaned_titles
titles_not_in_summarised = cleaned_titles - summarised_titles

# Print titles not common in cleaned_jsons.json
print("Titles not common in cleaned_jsons.json:")
for title in titles_not_in_cleaned:
    print(title)

# Print titles not common in summarised_topics.json
print("\nTitles not common in summarised_topics.json:")
for title in titles_not_in_summarised:
    print(title)
