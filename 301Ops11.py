#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Python File handling
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/08/2023
# Purpose:                      This code displays Python's file handling capabilities.                   
# Execution:                    31Ops10.py
# Resource:                     



import psutil
cpu_time = str (psutil.cpu_times())
print('CPU Time1: ' + cpu_time+ ".")

print(f'CPU Time2: {cpu_time}.')

print(psutil.cpu_times)
