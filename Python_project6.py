# Assignment 6: Lists and loops (for / while)
#
# In assignment 5 you used if/elif/else to make decisions about a single
# value. Real test runs have many test cases, so now you'll store several
# values in a list and use loops to process them one by one.
#
# Quick reference:
#   test_names = ["login_test", "logout_test"]   # a list
#   test_names[0]          -> "login_test"       # first item (index starts at 0)
#   len(test_names)        -> 2                  # number of items
#   test_names.append("x") -> adds "x" to the end
#   for name in test_names:                      # loop over every item
#       print(name)

# TODO 1:
# Create a list called test_cases with these five test names:
#   "login_test", "logout_test", "signup_test", "search_test", "checkout_test"
# Print the whole list, then print the first and the last item
# (hint: the last item is at index -1), then print how many test cases
# there are using len().


# TODO 2:
# Use a for loop to print each test case on its own line, numbered from 1:
#   1. login_test
#   2. logout_test
#   ...
# (hint: keep a counter variable, or look up enumerate(test_cases, 1))


# TODO 3:
# Create a second list called test_results with these values, in the same
# order as test_cases:
#   "pass", "fail", "pass", "pass", "fail"
# Loop over both lists together (use range(len(test_cases)) and an index,
# or look up zip()) and print a line for each test, e.g.:
#   login_test -> pass
# Use an if/else inside the loop so failed tests print with a warning:
#   logout_test -> FAIL  <-- needs investigation


# TODO 4:
# Count how many tests passed and how many failed using a for loop and two
# counter variables (passed_count, failed_count). Then calculate the pass
# percentage as a float:
#   pass_percentage = passed_count / len(test_results) * 100
# Print a summary line using an f-string, e.g.:
#   "Passed: 3, Failed: 2, Pass percentage: 60.0%"


# TODO 5:
# Use a while loop to let the user add new test cases at runtime:
#   - Ask "Enter a new test case name (or 'done' to finish): "
#   - If they type "done" (case-insensitive), stop the loop
#   - Otherwise append the name to test_cases
# After the loop ends, print the updated list and its new length.


# TODO 6 (bonus):
# Build a new list called failed_tests that contains only the names of the
# tests whose result is "fail" (loop + if + append). Print it.
# If failed_tests is empty, print "All tests passed!" instead.
#
# Reminder from assignment 4: keep this file to runnable Python only. If you
# want to share your terminal output, paste it inside comments (# ...) or in
# a separate notes file.
