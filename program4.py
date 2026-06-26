age = int(input("Enter age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# Output:
# Enter age: 25
# Adult
