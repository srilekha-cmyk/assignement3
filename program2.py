num = int(input("Enter a number: "))

if num >= 10 and num <= 20:
    print("Number is within the range")
else:
    print("Number is not within the range")

text = input("Enter a string: ")

if text != "" and len(text) > 5:
    print("Valid string")
else:
    print("Invalid string")

# Output:
# Enter a number: 15
# Number is within the range
# Enter a string: Python
# Valid string
