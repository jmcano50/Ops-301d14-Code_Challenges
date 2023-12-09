#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Python Conditional Statements
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/07/2023
# Purpose:                      Creat if Statements depending on conditions
# Execution:                    31Ops9.py
# Resource:                     https://chat.openai.com/share/e6863c53-9310-4ae7-a25a-58afd7380861

# Import

#Defines sets for ranks
junior_marine_ranks= {"Pvt", "Pfc", "Lcpl"}
nco_marine_ranks= {"Cpl", "Sgt"}
snco_marine_ranks= {"SSgt", "GySgt", "MSgt", "1stSgt", "MGySgt", "SgtMaj"}

#Conditions
equals_1 = junior_marine_ranks == nco_marine_ranks
not_equals_1 = junior_marine_ranks  != snco_marine_ranks
less_than1 = junior_marine_ranks != snco_marine_ranks 
less_than_or_equal_to_1 = "Cpl" in nco_marine_ranks
greater_than_1 = len(snco_marine_ranks) > len(nco_marine_ranks) 
greater_than_or_equal_to_1 = "Cpl" in nco_marine_ranks

# If statement with logical conditional
if equals_1:
    print("Condition 1 met.")
elif not_equals_1:
    print("Condition 2 met.") 
elif less_than1: 
    print("Condition 3 met.") 
elif less_than_or_equal_to_1:
    print("Condition 4 met.") 
elif greater_than_1:
    print("Condition 5 met.")
elif greater_than_or_equal_to_1:
    print("Condition 6 met.")
else:
    print("No conditions met.")

