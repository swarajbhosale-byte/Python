# Assignment 7: Functions (def, parameters, return)
#
# In assignment 6 you wrote loops to process a list of test cases and
# results. Some of that logic - like calculating a pass percentage - is
# something you'll want to reuse again and again. Functions let you give a
# block of code a name and call it whenever you need it.
#
# Quick reference:
#   def greet(name):                 # define a function with one parameter
#       return "Hello, " + name      # send a value back to the caller
#
#   message = greet("Swaraj")        # call it and store the returned value
#   print(message)                   # -> Hello, Swaraj
#
# print() vs return:
#   print() only shows a value on the screen.
#   return hands the value back so the caller can store it or use it further.
#   A function with no return statement gives back None.

# TODO 1:
# Write a function called print_banner() that takes no parameters and
# prints:
#   ==============================
#   Test Execution Report
#   ==============================
# Call it once.


# TODO 2:
# Write a function called calculate_pass_percentage(passed, total) that
# RETURNS (not prints) the pass percentage as a float:
#   passed / total * 100
# If total is 0, return 0.0 instead (dividing by zero would crash).
# Call it with (8, 10) and with (0, 0), store each result in a variable,
# and print both.


# TODO 3:
# Write a function called get_status(pass_percentage) that RETURNS a string
# using the same rules as assignment 5:
#   - 90 or above -> "Excellent"
#   - 70 up to 89.99 -> "Good"
#   - below 70 -> "Needs attention"
# Call it with 95, 75 and 40 and print each result.


# TODO 4:
# Write a function called count_results(results) that takes a list like:
#   ["pass", "fail", "pass", "pass", "fail"]
# Loop over it, count the passes and fails, and RETURN both counts:
#   return passed_count, failed_count
# When calling it, unpack both values at once:
#   passed, failed = count_results(test_results)
# Print both counts.


# TODO 5:
# Put it all together. Using the functions from TODOs 1-4:
#   - Create test_results = ["pass", "fail", "pass", "pass", "pass"]
#   - Call print_banner()
#   - Get passed/failed with count_results()
#   - Get the percentage with calculate_pass_percentage()
#   - Get the status with get_status()
#   - Print one summary line with an f-string, e.g.:
#     "Passed: 4, Failed: 1, Pass percentage: 80.0% -> Good"
# Notice how short this part becomes once the logic lives in functions.


# TODO 6 (bonus):
# Write a function called log_result(test_name, result="pass") that prints:
#   "[PASS] login_test"   or   "[FAIL] logout_test"
# (hint: result.upper() gives "PASS"/"FAIL")
# The parameter result has a default value of "pass", so you can call it
# without it. Call it like this and check the output:
#   log_result("login_test")
#   log_result("logout_test", "fail")
#
# Reminder: keep this file to runnable Python only. If you want to share
# your terminal output, paste it inside comments (# ...) or in a separate
# notes file.
