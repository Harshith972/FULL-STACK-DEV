#task 1
# for i in range(1,11):
#     print(i)

#task 2
# for i in range(1, 51):
#     if i%2==0:
#         print(i)

#task 3
# num=int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")

# #task 4
# sum=0
# for i in range(1,101):
#     sum+=i
#     print(sum)

#task 5
# name=input("enter a text:")
# count=0
# for charc in name:
#     if charc.lower()=='a' or charc.lower()=='e' or charc.lower()=='i' or charc.lower()=='o' or charc.lower()=='u':
#         count+=1

# print(f"vowels = {count}")

#while loop
#task 1
# num=int(input("Enter a number: "))
# while num>0:
#     print(num)
#     num-=1
#     if num==0:
#         print("time up")


#task 2
# correct_pin=8888
# count=3
# while count>0 :
#     pin=int(input("Enter your pin: "))
#     if pin==correct_pin:
#         print("login success")
#         break
#     else:
#         count-=1
#         print(f"try again only {count} attempts left")

# else:
#     print("maximum attempts reached, account locked")

#task 3
# password_correct="python123"
# while True:
#     password=input("enter password:")
#     if password==password_correct:
#         print("login success")
#         break
#     else:
#         print("wrong password, try again")
#         continue    

#task 4
# secret_number=7
# while True:
#     num=int(input("enter secret number:"))
#     if num==secret_number:
#         print("correct number")
#         break
#     else:
#         print("wrong number, try again")
#         continue

#task 5
# target=10000
# deposit=0
# while True:
#     add=int(input("enter amount to deposit:"))
#     deposit+=add
#     if deposit>=target:
#         print(f"target reached with{deposit}")
#         break

#loop+ break
#task1
# username="admin"
# password="admin123"
# while True:
#     user=input("enter username:")
#     psw=input("enter password:")

#     if psw==password and user==username:
#         print("login success")
#         break
#     else:
#         print("wrong credentials try again")

#task2
# products=["laptop","mobile","tablet","headphones"]
# while True:
#     product=input("enter product name:")
#     if product in products:
#         print(f"{product} is available")
#         break
#     else:
#         print(f"{product} is not available")
#         continue

#task 3
# students=[101,102,103,104,105]
# id=int(input("enter student id:"))

# for i in students:
#     if i==id:
#         print("student found")
#         break
# else:
#     print("student not found")

#task4
# logs = ["INFO", "INFO", "ERROR", "INFO", "ERROR", "INFO"]
# for log in logs:
#     if log=="ERROR":
#         print("first Error found, stopping the process")
#         break
#     else:
#         print("Processing log:", log)

#task5
# while True:
#     print("Menu")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Exit")
#     choice=int(input("enter your choice:"))



#     match choice:
#         case 1:
#             print("Deposit selected")
#         case 2:
#             print("Withdraw selected")
#         case 3:
#             print("Exit selected")
#             break
#         case _:
#             print("Invalid choice")

#loop+continnue
# numbers=[10, -5, 20, -8, 30]
# for num in numbers:
#     if num<0:
#         continue
#     print(num)

#task 4
# names=["Ravi", "", "John", ""]
# for name in names:
#     if name=="":
#         continue
#     print(name)

#task5
# while True:
#     pin=input("enter your pin:")
#     if len(pin)==4:
#         print("pin is valid")
#         break
#     else:
#         print("pin should be 4 digits")
#         continue

#nested loop
#task1

# letters=["A","B","C"]
# numbers=[1,2,3]
# for letter in letters:
#     for num in numbers:
#         print(f"{letter}{num}",end=" ")

#     print()

#task2
# students= ['s1','s2','s3','s4' ]
# subject=['sub1','sub2','sub3']
# for student in students:
#     for sub in subject:
#         marks=input(f"enter marks for {student} in {sub} ")
#         print(f"marks for {student} in {sub} is {marks}")

#task 3
# employees=['e1','e2','e3','e4','e5']
# days=['mon','tue','wed','thu','fri','sat','sun']
# for employee in employees:
#     for day in days:
#         attendence=input(f"enter attendence for {employee} on {day} : ")
#         print(f"attendence for {employee} on {day} is {attendence} : ")

#task 4
# servers=["web1", "web2", "db1"]
# services= ["Apache", "Docker", "Nginx"]
# for i in servers:
#     for j in services:
#         print(f" server {i} has service {j}")

#task 5
# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end=" ")
#     print()

#adv nested loop
#task 1
# customers=['c1','c2','c3']
# products=['p1','p2','p3','p4','p5']

# for i in customers:
#     sum=0
#     for j in products:
#         bill=int(input(f"enter bill for the customer {i} for the product {j} : "))
#         sum+=bill
#     print(f"total bill for the customer {i} is {sum}")

#task 2
# customers=['c1','c2','c3','c4','c5']
# #10 transactions each customer
# transactions=[100,200,300,400,500,600,700,800,900,1000]

# for i in customers:
#     for j in transactions:
#         print(f"customer {i} has transaction amount {j}")

# print("================================")

#task 3
# lines=[["info"]*99+["error"] for _ in range(10)]
# for line in lines:
#     print(line)

# print("================================")

# Correct answers for 10 questions
# correct_answers = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]

# students = []

# Get answers from 5 students
# for i in range(5):
#     print("\nStudent", i + 1)

#     answers = []

#     # Get 10 answers
#     for j in range(10):
#         ans = input(f"Question {j + 1} Answer (A/B/C/D): ").upper()
#         answers.append(ans)

#     students.append(answers)

# # Evaluate scores
# print("\nResults")
# for i in range(5):
#     score = 0

#     for j in range(10):
#         if students[i][j] == correct_answers[j]:
#             score += 1

#     print("Student", i + 1, "Score:", score, "/10")


#task 5 lms project
# students = ["Rahul", "Priya", "Amit"]
# courses = ["Python", "Java", "SQL", "AI"]

# # Store registered courses for each student
# registered = []

# for student in students:
#     print("\nStudent:", student)

#     student_courses = []

#     for course in courses:
#         choice = input(f"Register for {course}? (yes/no): ")

#         if choice.lower() == "yes":
#             student_courses.append(course)

#     registered.append(student_courses)

# # Display Report
# print("\n----- LMS Report -----")

# for i in range(len(students)):
#     print("\nStudent:", students[i])
#     print("Courses:", registered[i])
#     print("Course Count:", len(registered[i]))

#ATM
# Login Details
username = "admin"
password = "1234"

# Account Details
balance = 1000
transactions = []

# Login
user = input("Enter Username: ")
pwd = input("Enter Password: ")

if user == username and pwd == password:
    print("\nLogin Successful!")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Check")
        print("4. Transaction History")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            transactions.append("Deposited ₹" + str(amount))
            print("Deposit Successful!")

        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                transactions.append("Withdrawn ₹" + str(amount))
                print("Withdrawal Successful!")
            else:
                print("Insufficient Balance!")

        elif choice == 3:
            print("Current Balance: ₹", balance)

        elif choice == 4:
            print("\nTransaction History")

            if len(transactions) == 0:
                print("No Transactions Yet.")
            else:
                for transaction in transactions:
                    print(transaction)

        elif choice == 5:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Invalid Username or Password!")