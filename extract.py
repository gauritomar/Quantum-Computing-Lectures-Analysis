import os
import openai
import json
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI-API-KEY")
client = openai.Client(api_key=api_key)
context = '''
I will provide with you a transcript of an online lecture. You will be required to classify this lecture
based on the syllabus of the course.
Here is the complete course syllabus:
UNIT-I 10 Hours

Introduction to Quantum Computation: Classical deterministic systems, classical probabilistic
systems, quantum systems, basic quantum theory. Quantum bits, Bloch sphere representation of a
qubit, multiple qubits.

Background Mathematics and Physics: Hilber space, Probabilities and measurements, entan-
glement, density operators and correlation, basics of quantum mechanics, Measurements in bases

other than computational basis.

UNIT-II 11 Hours
Quantum Circuits: single qubit gates, multiple qubit gates, design of quantum circuits, classical
gates, quantum gates.

Quantum Information and Cryptography: Comparison between classical and quantum informa-
tion theory. Bell states. Quantum teleportation. Quantum Cryptography, no cloning theorem.

Asymmetric and symmetric encryption, quantum key distribution.

UNIT-III 11 Hours

Quantum Algorithms: Classical computation on quantum computers. Relationship between quan-
tum and classical complexity classes. Quantum circuits, reversibility of quantum circuits, power of

quantum algorithms, Deutsch’s algorithm, Deutsch’s-Jozsa algorithm, Shor factorization, Grover
search, applications of quantum algorithms.

UNIT-IV 10 Hours
Noise and error correction: Graph states and codes, Quantum error correction, fault-tolerant
computation, Single-Qubit Errors, Quantum Operations and Krauss Operators, The Depolarization
Channel, The Bit Flip and Phase Flip Channels, Amplitude Damping, Phase Damping.

You are required to classify the lecture into a unit and also give me a list of subtopics that were covered in this lecture.'''

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


def parse_vtt(file_path):
    subtitles = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        subtitle = None
        for line in lines:
            line = line.strip()
            if line.isdigit():
                # This is the subtitle index, ignore it
                continue
            elif '-->' in line:
                # This line contains the time stamps of the subtitle
                if subtitle:
                    subtitles.append(subtitle)
                subtitle = {'start': line.split(' --> ')[0], 'end': line.split(' --> ')[1], 'text': ''}
            elif subtitle is not None and 'Karuna Kadian' not in line:
                # This line contains the text of the subtitle and doesn't contain "Karuna Kadian"
                subtitle['text'] += line + ' '
        if subtitle:
            subtitles.append(subtitle)
    return subtitles

summarised_lectures = []

def process_vtt_files(folder_path):
    for filename in tqdm(os.listdir(folder_path)):
        if filename.endswith('.vtt'):
            file_path = os.path.join(folder_path, filename)
            subtitles = parse_vtt(file_path)
            text = ""
            for subtitle in subtitles:
                text += subtitle['text'] + ""
            topics = get_topics(text)
            summarised_lectures.append({"title": filename, "text": text, "topics": topics})
            


folder_path = 'Subtitles'  
process_vtt_files(folder_path)

output_file = 'summarised_topics.json'
with open(output_file, 'w') as f:
    json.dump(summarised_lectures, f)

print(f"Summarised topics are saved to {output_file}")