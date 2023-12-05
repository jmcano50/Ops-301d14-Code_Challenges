# Import the 'os' module
import os

# Declare and initialize variables
variable1 = "GySgtCPD"
Variable2 = 50
Variable3 = True

# Print the variables
print("Variable 1:", variable1)
print("Variable 2:", Variable2)
print("Variable 3:", Variable3)

# Execute bash commands using the 'os' module
# Command 1: whoami
whoami_result = os.popen("whoami").read()
print("UserLogIn: \n", whoami_result)

ip_result = os.popen("ip a").read()
print("IP addresses: \n", ip_result)

# Command 3: lshw -short
lshw_result = os.popen("sudo lshw -short").read()
print("Hardware information:\n", lshw_result)