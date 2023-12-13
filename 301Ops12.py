#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Python Requests Library
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/13/2023
# Purpose:                      Security professional use to evaluate how a web server responds to outside requests.
# Execution:                    31Ops12.py
# Resources:                    OpenAI. (2023). ChatGPT [Large language model]. https://chat.openai.com

# Import the requests library
import requests

# Ask the user for the URL
url = input("Please enter the URL you want to request: ")

# Present the available HTTP methonds and ask the user to choose one
print("Available HTTP methods: 1. GET 2. POST 3. PUT 4. DELETE")
method_number = input("Please enter the number for the HTTP method you want to use (1-4): ")

# Map the user input to an actual HTTP method
methods = {'1': 'GET', '2': 'POST', '3': 'PUT', '4': 'DELETE'}
method = methods.get(method_number, 'GET') # Defoult to 'GET' if the input is not recognized

# Confirm the request with the user
print(f"You have chosen to make a {method} request to {url}")
confirm = input("Do you want to proceed? (yes/no): ").strip().lower()

# If confirmed, perform the request
if confirm == 'yes':
    # Perform the request using the chosen method
    response = requests.request(method, url)

    # Check the status code and print a custom message
    if response.status_code == 200:
        print("Success! The request was successful.")
    elif response.status_code == 404:
        print("Error: The resource was not found.")
    else:
        print(f"The server responded with status code: {response.status_code}")

    # Print the response headers
    print("Response Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
    else:
        print("Request cancelled.")

