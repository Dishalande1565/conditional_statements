
# 1. Write a program to check whether a number is positive or negative.


num = int(input("Enter Your Number :"))
if num>0 :
    print("Positive")
elif num<0:
    print("Negative")
else :
    print("zero")


# 2. Write a program to check whether a number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Write a program to check whether a person is eligible to vote or not.

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 4. Write a program to check whether a number is greater than 100 or not.

num = float(input("Enter a number: "))
if num > 100:
    print("Greater than 100")
else:
    print("Not greater than 100")


#  5. Write a program to check whether a given year is a leap year or not.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 6. Write a program to compare two numbers and print the greater one.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater.")
elif num2 > num1:
    print(f"{num2} is greater.")
else:
    print("Both numbers are equal.")


# 7. Write a program to check whether a character is a vowel or consonant.

char = input("Enter a single character: ").lower()
if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")


# 8. Write a program to check whether a number is divisible by 5 or not.

num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# 9. Write a program to check whether a student has passed or failed (pass marks = 40).

marks = float(input("Enter marks: "))
if marks >= 40:
    print("Passed")
else:
    print("Failed")


# 10. Write a program to check whether a number is a single-digit number or not.

num = int(input("Enter a number: "))
if -9 <= num <= 9:
    print("Single-digit number")
else:
    print("Not a single-digit number")


# 11. Write a program to check whether a temperature is hot (>30) or cold.

temp = float(input("Enter temperature in Celsius: "))
if temp > 30:
    print("Hot")
else:
    print("Cold")

# 12. Write a program to check whether a person is a child or adult (age < 18).

age = int(input("Enter age: "))
if age < 18:
    print("Child")
else:
    print("Adult")


# 13. Write a program to check whether a number is zero or non-zero.

num = float(input("Enter a number: "))
if num == 0:
    print("Zero")
else:
    print("Non-zero")

# 14. Write a program to check whether a given character is uppercase or lowercase.


char = input("Enter a character: ")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
else:
    print("Not an alphabetic letter")

# 15. Write a program to check whether a number is divisible by both 3 and 7 or not.

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")

# 16. Write a program to find the greatest of three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the greatest.")
elif b >= a and b >= c:
    print(f"{b} is the greatest.")
else:
    print(f"{c} is the greatest.")

# 17. Write a program to check grade based on marks (A, B, C, Fail).

marks = float(input("Enter your marks: "))
if marks >= 85:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# 18. Write a program to check whether a number is positive, negative, or zero.

num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 19. Write a program to print the day name based on day number (1–7).

day = int(input("Enter day number (1-7): "))
if day == 1: print("Monday")
elif day == 2: print("Tuesday")
elif day == 3: print("Wednesday")
elif day == 4: print("Thursday")
elif day == 5: print("Friday")
elif day == 6: print("Saturday")
elif day == 7: print("Sunday")
else: print("Invalid day number")

# 20. Write a program to check ticket price based on age.

age = int(input("Enter age: "))
if age < 5:
    print("Ticket price: Free")
elif age <= 12:
    print("Ticket price: $5")
elif age <= 60:
    print("Ticket price: $10")
else:
    print("Ticket price: $7 (Senior Discount)")

# 21. Write a program to find the smallest of three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= b and a <= c:
    print(f"{a} is the smallest.")
elif b <= a and b <= c:
    print(f"{b} is the smallest.")
else:
    print(f"{c} is the smallest.")

# 22. Write a program to check salary bonus based on years of service.

salary = float(input("Enter current salary: "))
years = int(input("Enter years of service: "))

if years > 10:
    bonus = 0.10 * salary
elif years >= 5:
    bonus = 0.05 * salary
else:
    bonus = 0.02 * salary

print(f"Your bonus is: ${bonus:.2f}")

# 23. Write a program to calculate electricity bill based on units consumed.

units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
else:
    bill = (100 * 1.5) + (200 * 2.5) + ((units - 300) * 4.0)

print(f"Total Electricity Bill: ${bill:.2f}")


# 24. Write a program to check exam results (Distinction, First Class, Pass, Fail).

marks = float(input("Enter marks out of 100: "))
if marks >= 75:
    print("Result: Distinction")
elif marks >= 60:
    print("Result: First Class")
elif marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")


# 25. Write a program to check whether a triangle is equilateral, isosceles, or scalene.

s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

if s1 == s2 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# 26. Write a program to check month names based on month number.

month = int(input("Enter month number (1-12): "))
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

if 1 <= month <= 12:
    print(months[month - 1])
else:
    print("Invalid month number")

# 27. Write a program to check login status based on username and password.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secure123":
    print("Login Successful")
else:
    print("Invalid Credentials")

# 28. Write a program to calculate discounts based on total shopping amount.

amount = float(input("Enter total shopping amount: "))
if amount >= 1000:
    discount = 0.2 * amount
elif amount >= 500:
    discount = 0.1 * amount
else:
    discount = 0

print(f"Discount: ${discount:.2f}")
print(f"Total Amount after Discount: ${amount - discount:.2f}")


# 29. Write a program to check blood donation eligibility based on age and weight.

age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
if age >= 18 and age <= 65 and weight >= 50:
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")


# 30. Write a program to check the type of number (single, double, or three digit).

n = int(input("Enter a number: "))
if n < 0:
    n = -n
if n < 10:
    print("Single digit number")
elif n < 100:
    print("Double digit number")
elif n < 1000:
    print("Three digit number")
else:
    print("More than three digits")

# 31. Write a program to check whether a number is positive and even using nested if.

n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is positive but odd")
else:
    print("Number is not positive")


# 32.Write a program to check whether a student is eligible for an exam (attendance + marks).

attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))
if attendance >= 75 and marks >= 40:
    print("Eligible for the exam")
elif attendance < 75 and marks < 40:
    print("Not eligible: low attendance and low marks")
elif attendance < 75:
    print("Not eligible: low attendance")
else:
    print("Not eligible: low marks")


# 33. Write a program to check whether a person can apply for a loan.

age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
if age >= 21 and age <= 60:
    if income >= 25000:
        print("You can apply for the loan")
    else:
        print("Income is too low to apply")
else:
    print("Age must be between 21 and 60 to apply")


# 34. Write a program to check whether a year is a leap year and century year.


year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
 
if year % 100 == 0:
    print(year, "is a century year")
else:
    print(year, "is not a century year")


# 35. Write a program to check whether a number is divisible by 3 and 5.

n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3 only")
elif n % 5 == 0:
    print("Divisible by 5 only")
else:
    print("Not divisible by 3 or 5")


# 36. Write a program to check whether a person is eligible for a driving license.

age = int(input("Enter age: "))
test = input("Passed the driving test? (yes/no): ")
if age >= 18:
    if test == "yes":
        print("Eligible for a driving license")
    else:
        print("Pass the driving test first")
else:
    print("Not eligible: must be at least 18 years old")

# 37. Write a program to check whether a number lies between 10 and 50.

n = int(input("Enter a number: "))
if n >= 10 and n <= 50:
    print("Number lies between 10 and 50")
else:
    print("Number does not lie between 10 and 50")


# 38. Write a program to check whether a student passed all subjects.

m1 = float(input("Marks in subject 1: "))
m2 = float(input("Marks in subject 2: "))
m3 = float(input("Marks in subject 3: "))
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Passed all subjects")
else:
    print("Failed in one or more subjects")


# 39. Write a program to check whether a number is greater than 0 and less than 100.

n = float(input("Enter a number: "))
if n > 0 and n < 100:
    print("Number is greater than 0 and less than 100")
else:
    print("Condition not satisfied")


# 40. Write a program to check whether a password is valid using nested if.

username = input("Enter username: ")
password = input("Enter password: ")
confirm = input("Confirm password: ")
if len(password) >= 8:
    if password == confirm:
        if password != username:
            print("Valid password")
        else:
            print("Invalid: password cannot be the same as username")
    else:
        print("Invalid: passwords do not match")
else:
    print("Invalid: password must be at least 8 characters")


# 41. Write a program to print weekday name using match case.

day = int(input("Enter day number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")


# 42. Write a program to perform calculator operations using match case.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")


# 43. Write a program to print month days using match case.

month = int(input("Enter month number (1-12): "))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        year = int(input("Enter year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29 days")
        else:
            print("28 days")
    case _:
        print("Invalid month")


# 44. Write a program to check traffic signal actions using match case.

color = input("Enter signal color (red/yellow/green): ")
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal color")


# 45. Write a program to print menu-based food selection using match case.

print("1. Pav Bhaji")
print("2. Misal Pav")
print("3. Vada Pav")
print("4. Poha")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("You selected Pav Bhaji")
    case 2:
        print("You selected Misal Pav")
    case 3:
        print("You selected Vada Pav")
    case 4:
        print("You selected Poha")
    case _:
        print("Invalid choice")


# 46. Write a program to print grade description using match case.

grade = input("Enter grade (A/B/C/D/F): ")
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very good")
    case "C":
        print("Good")
    case "D":
        print("Needs improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")


# 47. Write a program to check user role (admin, user, guest) using match case.

role = input("Enter role (admin/user/guest): ")
match role:
    case "admin":
        print("Full access to the system")
    case "user":
        print("Limited access")
    case "guest":
        print("View-only access")
    case _:
        print("Unknown role")


# 48. Write a program to print language choice using match case.

print("1. English")
print("2. Hindi")
print("3. Marathi")
choice = int(input("Choose your language: "))
match choice:
    case 1:
        print("Hello! Welcome.")
    case 2:
        print("Namaste! Swagat hai.")
    case 3:
        print("Namaskar! Swagat aahe.")
    case _:
        print("Invalid choice")


# 49. Write a program to print result status using match case.

status = input("Enter result status (pass/fail/absent/withheld): ")
match status:
    case "pass":
        print("Congratulations, you passed!")
    case "fail":
        print("Better luck next time")
    case "absent":
        print("You were absent for the exam")
    case "withheld":
        print("Result is withheld, contact the office")
    case _:
        print("Invalid status")


# 50. Write a program to build a simple ATM menu using a match case.

balance = 10000
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Balance:", balance)
    case 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print("Deposited. New balance:", balance)
        else:
            print("Invalid amount")
    case 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Please collect your cash. New balance:", balance)
        else:
            print("Invalid amount or insufficient balance")
    case 4:
        print("Thank you for using the ATM")
    case _:
        print("Invalid choice")





