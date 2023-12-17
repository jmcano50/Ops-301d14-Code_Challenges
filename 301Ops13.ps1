# Script Name:                  Ops Challenge: Powershell AD Automation
# Author:                       Juan Miguel Cano
# Date of latest revision:      12/13/2023
# Purpose:                      To create a new user in Active Directory using PowerShell.

# Import the ActiveDirectory module
Import-Module ActiveDirectory

# User details
$username = "FranzFerdinand" 
$firstName = "Franz" 
$lastName = "Ferdinand" 
$ouPath = "OU=Domain Controllers,DC=corp,DC=globexpower,DC=com" # This is the OU path
$email = "ferdi@GlobeXpower.com" 
$title = "TPS Reporting Lead" 
$office = "Springfield, OR"

# Attempt to create the user
try {
    # Creating the user
    $newUser = New-ADUser -Name $username `
        -GivenName $firstName `
        -Surname $lastName `
        -UserPrincipalName "$email" `
        -EmailAddress $email `
        -Title $title `
        -Office $office `
        -Path $ouPath `
        -Enabled $true `
        -AccountPassword (Read-Host -AsSecureString "Enter Password") `
        -PassThru

    # Enable the new user account
    Enable-ADAccount -Identity $newUser

    # Output confirmation
    Write-Host "User $username created successfully."
} catch {
    Write-Host "Error creating user: $_"
}
