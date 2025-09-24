import requests

# Replace with your actual question
question = "You are given an array of integers. Return the sum of two numbers equal to target."

# Send POST request to Flask backend
response = requests.post("http://127.0.0.1:5000/predict", json={"question": question})

# Print response from the API
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
