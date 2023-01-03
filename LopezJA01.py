#LopezJA01.py

"""
Name: Jason Lopez
Date: October 13th, 2022
Class: CSEC 1436 | Assignment 01
Purpose: Write a program that determines the maximum time it takes to hack a combination lock using brute force.
         A lock can have 3,4,5 or more rings which have to be twirled to open the lock. 
         Each ring consists of a number from 0 to 9.

Pseudo Code:

1. Print output statement that introduces the program.
2. Create a while loop to get user input of minimum rings. This will error check as well.
3. Create a while loop to get user input of maximum rings. This will error check as well.
4. Create a error check for my for loop when user inputs proper float numbers.
5. Use for loop with proper math calculations to bruteforce and find timings of the lock combos.
"""

print("Welcome to the program that determines the time in takes to hack a combination lock.\n\n" 

"A lock can have 3, 4, 5 or more rings which have to be twirled to open the lock.\n"
"Each ring consists of a number from 0 to 9.\n\n"

"You will be asked to enter the minimum and maximum number of rings a lock can have.\n"
"Then for each, you will be asked to enter the average time it takes to twirl the rings to try opening the lock.\n"
"The program will print the maximum time it takes in days, hours, minutes, and seconds to open each type of lock.\n\n")

# User input of the minimum number of rings on the lock + error checks.
while True:
    min_num_rings = int(input("Enter the minimum number of rings on a lock (number must be >= 3 but <= 4): "))
    if min_num_rings >= 3 and min_num_rings <=4:
        break
    else:
        print(f"**Error** You have entered {min_num_rings} which is not a number between 3 and 4. Please enter again")

# User input of the maximum number of rings on the lock + error checks.
while True:
    max_num_rings = int(input("Enter the maximum number of rings on a lock (number must be >= minimum rings but less than 10): "))
    if max_num_rings >= 3 and max_num_rings <=10:
        break
    else:
        print(f"**Error** You have entered {max_num_rings} which is not a number between 3 and 10. Please enter again")

# Error check if the user inputs a zero, negative number, or anything higher/below the required input.
error = False
while not error:
    for i in range(min_num_rings, max_num_rings+1):     # Use math to calculate the time, and use it to calculate how fast we can bruteforce lock combos.
        time_in_seconds = float(input(f"Enter the time in seconds (float between 0 and and 10.0) it takes to set the rings for a {i} ring lock (Example: 1.6): "))        
        if time_in_seconds >=0 and time_in_seconds <=10:
            max_sec = (10 ** i) * time_in_seconds

            max_day = int(max_sec // 86400) 
            day_remainder = max_sec % 86400

            max_hours = int(day_remainder // 3600)
            hours_remainder = max_sec % 3600

            max_min = int(hours_remainder // 60)
            min_remainder = int(max_sec % 60)

            print(f"Maximum time_in_seconds to break {i} ring combination lock: {max_day} d {max_hours} h {max_min} m {min_remainder} s")
            error = True
        else:
            print(f"**Error** You have entered {time_in_seconds} which is not a number between 0 and 10.0. Please enter again")
            error = False
            break