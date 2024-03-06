# Quantum Computing Lectures Analysis

This repository contains scripts and tools for analyzing the old quantum computing lectures. Its hard to parse through all of them and get to the exact subtopic especially when tomorrow is the midsem.

1. **.gitignore**: Updated Gitignore file to prevent the inclusion of JSON and TXT files in the repository.

2. **analyse_topic.py**: Analyse the jsons created by **extract.py** and validate it into json objects for further rendering.

3. **cross_check.py**: A Python script to verify that no lectures are missing from the analysis, ensuring completeness of the data.

4. **cross_verify.py**: Similar to cross_check.py, this script verifies the completeness of lectures in the analysis.

5. **extract.py**: Python script responsible for extracting data from the .vtt subtitle files, cleaning it, running it through the openai api and getting an unformatted json object for each.

6. **index.html**: HTML file for displaying cleaned JSON data as an HTML table. This file is intended for visualization purposes and make a pdf from to send on the group.

7. **one_missing.py**: Python script that addresses and fixes missing lectures identified during the analysis.

8. **server.js**: JavaScript file for serving the HTML file as a web page to visualize the cleaned JSON data.
