#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Install Psutil
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/12/2023
# Purpose:                      Create a Python script that fetches this information using Psutil
# Execution:                    31Ops10.py
# Resources:                    https://chat.openai.com/share/f3c1d4af-ea60-45c1-8309-8f3f389a2fdf

import psutil

def fetch_cpu_times():
    # Get CPU times
    cpu_times = psutil.cpu_times()

    # Extracting the required information
    return {
        'Time spent by normal processes in user mode': cpu_times.user,
        'Time spent processes in kernel mode': cpu_times.system,
        'Time when system was idle': cpu_times.idle,
        'Time spent by priority processes in user mode': cpu_times.nice,
        'Time spent for servicing hardware interrupts': cpu_times.iowait,
        'Time spent for servicing software interrupts': cpu_times.irq,
        'Time spent by other operating systems in a virtualized environment': cpu_times.steal,
        'Time spent running a virtual CPU for guest OS under the control of the Linux kernel': cpu_times.guest
    }

# Call the function and print the results
try:
    cpu_times_info = fetch_cpu_times()
    for key, value in cpu_times_info.items():
        print(f"{key}: {value} seconds")
except Exception as e:
    print(f"An error occurred: {e}")
