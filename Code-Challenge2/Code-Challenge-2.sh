#!/bin/bash

# Script Name:                  Ops Challenge: File Permissions
# Author:                       Juan Miguel Cano
# Date of latest revision:      11/29/2023
# Purpose:                      Demo variables / and functions
# Execution:                    bash Code-Challenge-2.sh or ./Code-Challenge-2.sh
# Resources:                    https://chat.openai.com/share/02f84995-664d-4f5b-9950-061bb320a8b9

# Function to display an error message and exit
function error_exit {
    echo "Error: $1"
    exit 1
}

# Prompt the user for the directory path
read -p "Enter the directory path: " directory

# Check if the directory is valid
if [ ! -d "$directory" ] || [ ! -x "$directory" ]; then
    error_exit "Invalid directory path or no execute permission."
fi

# Prompt the user for the permission number
read -p "Enter the permission number (e.g., 777): " permission

# Validate the permission input
if [[ ! "$permission" =~ ^[0-7]{3}$ ]]; then
    error_exit "Invalid permission format. Please enter a three-digit number (e.g., 777)."
fi

# Change permissions for each file in the directory with a slight delay
echo -e "\nChanging permissions..."
for file in "$directory"/*; do
    if [ -f "$file" ]; then
        old_permissions=$(stat -c "%a" "$file")
        chmod "$permission" "$file"
        echo "Changed permissions for: $file (Old: $old_permissions, New: $permission)"
        sleep 0.1
    fi
done

# Print the directory contents and new permissions
echo -e "\nDirectory Contents:"
ls -l "$directory"

echo "Permissions changed successfully."
