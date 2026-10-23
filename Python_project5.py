# Assignment 5: Conditionals (if / elif / else)
#
# In assignment 4 you collected tester_name, test_cases_executed,
# pass_percentage, and automation_ready_input using input().
# Now you'll use conditionals to make decisions based on values like these.
#
# Reminder: input() always returns a string - cast with int()/float() where
# the TODOs below need a number.

# TODO 1:
# Ask the user to enter the pass percentage (input + float()).
# Store it in pass_percentage, then use if/elif/else to print a message:
#   - 90 or above       -> "Excellent pass rate!"
#   - 70 up to 89.99    -> "Good pass rate, but room for improvement."
#   - below 70          -> "Pass rate needs attention."


# TODO 2:
# Ask "Is automation ready? (yes/no): " using input().
# Store the raw answer in automation_ready_input.
# Convert it to a real boolean named automation_ready:
#   - True if the user typed "yes" (case-insensitive)
#   - False otherwise
# Print automation_ready and print(type(automation_ready)) to confirm it's
# an actual bool now, not just a string.


# TODO 3:
# Ask the user to enter the number of test cases executed (input + int()).
# Store it in test_cases_executed, then use if/elif/else to print:
#   - 0           -> "No tests were executed."
#   - 1 to 4      -> "Only a few tests were executed - consider adding more."
#   - 5 or more   -> "Good test coverage."


# TODO 4:
# Combine conditions using `and` / `or`.
# If pass_percentage >= 90 AND automation_ready is True, print:
#   "This suite is ready for CI integration!"
# Otherwise print:
#   "Not ready for CI yet."


# TODO 5 (bonus):
# Ask the user to enter a test case priority as a number:
#   1 = High, 2 = Medium, 3 = Low
# Convert it to an int, then use if/elif/else to print the matching label
# ("High priority", "Medium priority", "Low priority").
# If the number isn't 1, 2, or 3, print "Invalid priority entered."


# Review (Swati): This assignment hasn't been attempted yet - there's no
# code under any of the TODOs, only the instructions. Please add your
# solution below each TODO (or all together at the bottom, like you did in
# assignment 4). A few pointers before you start:
#
# - TODO 1: order matters in if/elif/else. Check the highest range first
#   (>= 90), then >= 70, then else - Python stops at the first match, so
#   you don't need "and < 90" on the second condition.
# - TODO 2: to make "yes", "Yes" and "YES" all count, compare a lowercased
#   copy: automation_ready_input.lower() == "yes". That comparison already
#   gives you a real True/False - no if/else needed to build the bool.
# - TODO 3: use == for the 0 check (a single = is assignment and will give
#   a SyntaxError inside an if).
# - TODO 4: automation_ready is already a bool, so "and automation_ready"
#   is enough - no need for "== True".
# - TODO 5: remember to cast with int() first; "1" (string) is not equal
#   to 1 (int), so comparing the raw input() result would never match.
#
# Same reminder as assignment 4: keep this file to runnable Python only.
# If you want to include your test-run output, put it in comments (# ...),
# not as bare text, so the file still runs.
