# Review (Swati): Good - all four basic types (str, int, float, bool) are
# covered and each one is verified with type(). This is exactly what the
# assignment asked for.

tester_name = "Swaraj"

print(tester_name)


# Python automatically knows the type of data stored in a variable.

# 1. str = String (text)
test_name = "login_test"
print(test_name)
print(type(test_name))


# 2. int = Integer (whole number)
test_cases = 5
print(test_cases)
print(type(test_cases))


# 3. float = Decimal number
# Review (Swati): minor nit - "success_rate" reads like a percentage, but
# 9.8 isn't one on its own (e.g. 9.8%% or 9.8/10?). Not wrong, just pick a
# value/name pair that's unambiguous next time (e.g. 98.0 for a % rate).
success_rate = 9.8
print(success_rate)
print(type(success_rate))


# 4. bool = Boolean (True or False)
test_passed = True
print(test_passed)
print(type(test_passed))
