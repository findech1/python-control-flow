def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
print(large_power(10, 3))  # Output: False
print(large_power(10, 4))  # Output: True
