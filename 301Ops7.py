#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Directiory Creation
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/05/2023
# Purpose:                      Traverse through directories, subdirectories and files in the provided path 
# Execution:                    31Ops7.py
# Resource:                     



# Import libraries

import os

def generate_directory_structure():
    # Ask the user for a directory path
    user_input_path = input("Enter a directory path: ")

    # Check if the provided path exists
    if not os.path.exists(user_input_path):
        print("Error: The specified path does not exist.")
        return

    #Use os.walk() to get all directories, sub-directores, and files
    for root, dirs, files in os.walk(user_input_path):
        print(f"Current directory: {root}")
        print(f"Subdirectories: {dirs}")
        print(f"Files: {files}")

# Call the function to generate and display the directory structure
generate_directory_structure()

