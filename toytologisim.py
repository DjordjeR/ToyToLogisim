################################################
# Created by Djordje Rajic for needs in RO
# course. Convert .toy file to logisim file
# DISCLAIMER
# This is not an official program, it is quick
# solution for a problem that was at hand
# feel free to improve this program.
#################################################


import os.path  # We need to check if file exists
import sys  # For reading command line arguments

listCom = []
listNum = []
newListNum = []

line_argument_count = len(sys.argv)

if line_argument_count != 2:
    print("[ERROR] Wrong usage")
    print("python3 toytologisim.py file_name.toy")
    print("python3 toytologisim.py file_name.toy > out_file.lsim")
    exit(-1)

filename = sys.argv[1]  # Take file name from command line
# Check if file exists
if not os.path.isfile(filename):
    print("File does not exist!")
    exit(-1)

# Open file and save values after space in list
# TODO: We should really check if file is valid
with open(filename, 'r') as file:
    for row in file:
        number, command = row.split()
        listCom.append(command)
        listNum.append(number)

# We need to get rid of : in our numbering, this step is not
# necessary but it makes me feel better

for num in listNum:
    newListNum.append(num.replace(":", ""))

# Print out the code
print("v2.0 raw")
print("16*0")
for line in listCom:
    print(line)