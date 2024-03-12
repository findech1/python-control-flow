def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

number1 = 20
number2 = 35

result1 = divisible_by_ten(number1)
result2 = divisible_by_ten(number2)

print(f"{number1} is divisible by 10: {result1}")
print(f"{number2} is divisible by 10: {result2}")