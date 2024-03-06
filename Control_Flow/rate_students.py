#Python program to rate students' performance:
def rate_performance(score):
    if score >= 80:
        return "Distinction"
    elif 70 <= score < 80:
        return "Credit"
    elif 50 <= score < 60:
        return "Fair"
    else:
        return "Fail"

# Test the function
score = float(input("Enter the student's score: "))
result = rate_performance(score)
print("Result:", result)

