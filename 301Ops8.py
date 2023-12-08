#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Python Collections
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/06/2023
# Purpose:                      demonstrate the manipulation of lists and the use of various list methods, including basic operations and involving tuples, sets, and dictionaries.                    
# Execution:                    31Ops8.py
# Resource:                     https://chat.openai.com/share/73de1c97-4634-4849-8003-6906aefc1f33
                     

# Step 1: Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:10])

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)

# Use the index() method to find the index of a specific element
index_SSgt = original_list.index("SSgt")
print("Index of 'SSgt':", index_SSgt)

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)

# Use the remove() method to remove a specific element
original_list.remove("SSgt")
print("List after removing 'SSgt':", original_list)

# Use the reverse() method to reverse the order of elements in the list
original_list.reverse()
print("Reversed list:", original_list)

# Use the sort() method to sort the elements in the list
original_list.sort()
print("Sorted list:", original_list)

# Create a tuple
my_tuple = ("Pvt", "Pfc", "LCpl")

# Create a set
my_set = {"Pvt", "Pfc", "LCpl"}

# Create a dictionary
my_dict = {"Marines1": "Pvt", "Marines2": "Pfc", "Marines3": "LCpl"}

# Print the created tuple, set, and dictionary
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)