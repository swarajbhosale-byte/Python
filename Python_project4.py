# Assignment 4: input() and user interaction
#
# So far we've hardcoded values like tester_name and test_cases_executed.
# In this assignment, you'll take those values from the user at runtime
# using the input() function instead.
#
# Remember: input() always returns a string, even if the user types a number.
# You'll need to convert ("cast") it to the right type using int() or float()
# where needed.

# TODO 1:
# Ask the user to enter their name using input(), store it in tester_name,
# and print a greeting like: "Hello, Swaraj!"


# TODO 2:
# Ask the user to enter the number of test cases executed.
# input() gives you a string - convert it to an int using int().
# Store it in test_cases_executed and print it.


# TODO 3:
# Ask the user to enter the pass percentage (a decimal number, e.g. 85.5).
# Convert it to a float using float().
# Store it in pass_percentage and print it.


# TODO 4:
# Ask the user whether automation is ready by typing yes or no.
# Store their raw answer in a variable called automation_ready_input.
# Print out what they typed.
# (Don't worry about converting this to a real bool yet - that's for the
# next assignment on conditionals!)


# TODO 5 (bonus):
# Print a single summary line using an f-string that combines all four
# values, e.g.:
# "Swaraj executed 10 test cases with 85.5% pass rate. Automation ready: yes"


Code: 
tester_name = input("Enter your name: ")
print("Hello, " + tester_name + "!")

test_cases_executed = int(input("Enter the number of test cases executed: "))
print("Test cases executed:", test_cases_executed)

pass_percentage = float(input("Enter the pass percentage: "))
print("Pass percentage:", pass_percentage)

automation_ready_input = input("Is automation ready? (yes/no): ")
print("Automation ready:", automation_ready_input)

print(f"{tester_name} executed {test_cases_executed} test cases with {pass_percentage}% pass rate. Automation ready: {automation_ready_input}")

Terminal result
miko@miko-Lenovo-V130-14IKB:~$ /usr/local/bin/python3.14 /home/miko/Downloads/Python_project4.py
miko@miko-Lenovo-V130-14IKB:~$ /usr/local/bin/python3.14 /home/miko/Downloads/Python_project4.py
miko@miko-Lenovo-V130-14IKB:~$ /usr/local/bin/python3.14 /home/miko/Downloads/Python_project4.py
Enter your name: ^CTraceback (most recent call last):
  File "/home/miko/Downloads/Python_project4.py", line 4, in <module>
    test_cases_executed = int(input("Enter the number of test cases executed: "))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

miko@miko-Lenovo-V130-14IKB:~$ /usr/local/bin/python3.14 /home/miko/Downloads/Python_project4.py
Enter your name: Swaraj
Hello, Swaraj!
Enter the number of test cases executed: 100
Test cases executed: 100
Enter the pass percentage: 85 %
Traceback (most recent call last):
  File "/home/miko/Downloads/Python_project4.py", line 7, in <module>
    pass_percentage = float(input("Enter the pass percentage: "))
ValueError: could not convert string to float: '85 %'
miko@miko-Lenovo-V130-14IKB:~$ 85
85: command not found
miko@miko-Lenovo-V130-14IKB:~$ 85
85: command not found
miko@miko-Lenovo-V130-14IKB:~$ /usr/local/bin/python3.14 /home/miko/Downloads/Python_project4.py
Enter your name: Swaraj
Hello, Swaraj!
Enter the number of test cases executed: 100
Test cases executed: 100
Enter the pass percentage: 85
Pass percentage: 85.0
Is automation ready? (yes/no): Yes
Automation ready: Yes
Swaraj executed 100 test cases with 85.0% pass rate. Automation ready: Yes
miko@miko-Lenovo-V130-14IKB:~$ ^C
miko@miko-Lenovo-V130-14IKB:~$ 
