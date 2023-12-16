#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Powershell AD Automation
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/13/2023
# Purpose:                      To create a new user in Active Directory using PowerShell.
# Execution:                    31Ops13.py
# Resources:                    https://chat.openai.com/share/e5aeae62-9c9c-4395-adc3-854dc55de98d

# Active Directory user creation script for Franz Ferdinand

# User details
$username = "FranzFerdianad" 
$firstName = "Franz" 
$lastName = "Ferdinand" 
$ouPath = "OU=TPSDepartment,DC=GlobeX,DC=USA" # Update this with the correct Organizational Unit path
$email = "ferdi@GlobeXpower.com" 
$title = "TPS Reporting Lead" 
$office = "Springfield, OR"

# Creating the user
New-ADUser -Name $username `
    -GivenName $firstName `
    -Surname $lastName `
    -UserPrincipalName "$email" `
    -EmailAddress $email `
    -Title $title `
    -Office $office `
    -Path $ouPath `
    -Enabled $true `
    -AccountPassword (Read-Host -AsSecureString "Enter Password") `
    -PassThru | Enable-ADAccount

# Output confirmation
Write-Host "User $username created successfully."

