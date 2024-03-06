import json

with open("summarised_topics.json", "r") as file:
    summarised_topics = json.load(file)

for topic in summarised_topics:
    print(topic["title"])
    if topic["title"] == "Quantum Computing-20230424 0439-1"+".vtt":
        print(topic["topics"])
