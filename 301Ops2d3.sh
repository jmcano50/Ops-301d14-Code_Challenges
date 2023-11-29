#!/bin/bash

# Script Name:                  Ops Challenge: File Permissions
# Author:                       Juan Miguel Cano
# Date of latest revision:      11/29/2023
# Purpose:                      Demo variables / and functions
# Execution:                    bash demo.sh or ./demo.sh chmod -x demo.sh
# Resources:                    https://chat.openai.com/share/02f84995-664d-4f5b-9950-061bb320a8b9


# Prompt the user for the directory path
read -p "Enter the directory path: " directory 

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory not found."
    exit 1
fi    

# Prompt the user for the permission number
read -p " Enter the permission number (777): "permission

# Change permissions for each file in the directory with a slight delay
echo =e "\nChanging permission..."
for file in "$directory"/*; do
    if [ -f "$file" ];then
        chmod "$permission" "$file"
        echo "Changed permissions for: $file"
        sleep 0.1 # Adjust the delay time as needed
    fi
done

# Print the directory contents and new permissions
echo -e "\nDirectory Contents:"
ls -l "$directory"