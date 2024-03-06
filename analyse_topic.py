import json
from tqdm import tqdm
from dotenv import load_dotenv
import openai
import os
from tqdm import tqdm

load_dotenv()

api_key = os.getenv("OPENAI-API-KEY")
client = openai.Client(api_key=api_key)
context = '''
I am presenting unstructured text data to you. Return this data in a structured json format where the keys should be "unit" containing an integer and "subtopics" containing a list of strings.'''
def get_topics(text):
    try:
        completion= client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": text},
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print("An error occurred:", e)

def load_summarised_topics(json_file):
    with open(json_file, 'r') as f:
        summarised_topics = json.load(f)
    return summarised_topics


json_file = 'summarised_topics.json'  
summarised_topics = load_summarised_topics(json_file)

cleaned_topics =[]

for lecture in tqdm(summarised_topics):
    title = lecture["title"].replace('.vtt', '.mp4')
    cleaned_topic = {"title": title, "unstructured_text": lecture["topics"]}
    cleaned_json = get_topics(str(cleaned_topic))
    print(cleaned_json)
    
    try:
        json.loads(cleaned_json)
        if "title" not in cleaned_json.keys():
            cleaned_json["title"] = title
        cleaned_topics.append(cleaned_json)
    except json.JSONDecodeError:
        # If the JSON is not valid, save it to a text file
        with open("invalid_topics.txt", "a") as f:
            f.write(cleaned_json + "\n")

# Save valid JSON topics to a file
with open("cleaned_topics.json", "w") as f:
    json.dump(cleaned_topics, f, indent=4)


