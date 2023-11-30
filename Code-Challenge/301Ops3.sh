#!/bin/bash

# Script Name:                  Ops Challenge: File Permissions
# Author:                       Juan Miguel Cano
# Date of latest revision:      11/29/2023
# Purpose:                      Demo variables / and functions
# Execution:                    bash Code-Challenge-2.sh or ./Code-Challenge-2.sh
# Resources:                    https://chat.openai.com/share/02f84995-664d-4f5b-9950-061bb320a8b9
# Resources:                    Marcus Nogueira

# Declaration of function
Change-Permissions() {
    read -p "Enter the directory path: " directory
    read -p "Enter the input permissions number: " permission_number

    cd "$directory"
    chmod $permission_number *
    ls -l
}
# Calling the function
Change-Permissions 
