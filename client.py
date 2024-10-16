import requests

# Define the questions
questions = [
    "What is your name?",
    "How satisfied are you with our service (1-5)?",
    "Any comments or suggestions?"
]

# Collect responses
responses = {}
for question in questions:
    answer = input(question + " ")
    responses[question] = answer

# Upload responses to the server
try:
    response = requests.post("http://192.168.1.24:5000/submit", json=responses)
    if response.status_code == 200:
        print("Responses submitted successfully!")
    else:
        print("Failed to submit responses:", response.text)
except Exception as e:
    print("Error while submitting responses:", e)

