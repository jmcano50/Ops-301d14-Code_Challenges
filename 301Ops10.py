#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Python File handling
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/08/2023
# Purpose:                      This code displays Python's file handling capabilities.                   
# Execution:                    31Ops10.py
# Resource:                     https://chat.openai.com/share/aacba012-e2a9-428b-9768-a1a14391153b

import os # Add this import statement                   

# Step 1: Create a new .txt file
file_path ="example.txt"

#Step 2: Append three lines to the file
with open(file_path, "a") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Step 3: Read and print the first line
with open(file_path, "r") as file:
    first_line = file.readline()
    print("First line:", first_line.strip())

# Step 4: Delete the .txt file
try:
    # Delete the .txt file
    os.remove(file_path)
    print("File deleted successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

