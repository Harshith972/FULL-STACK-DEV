
#TASK 1
# num= int(input("Enter a number: "))
# if num>0:
#     print("The number is positive.")
# elif num<0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")


#TASK 2
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

#TASK 3
# amount=int(input("Enter the amount: "))
# if amount>5000:
#     print("Coupon Applied")
# else:
#     print("Coupon cannot be Applied for amount less than 5000")

#TASK 4
# value=int(input("Enter order value: "))
# if value>1000:
#     print("Free Delivery Available")
# else:
#     print("Delivery charges are applicable")

#task 5
# username=input("Enter your username: ")
# if username=="admin":
#     print("Welcome Admin")
# else:
#     print("Welcome User")

#task 1
# num=int(input("Enter a number: "))
# if num%2==0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


#task 2
# actual_pin=1234
# entered_pin=int(input("Enter your pin: "))
# if entered_pin==actual_pin:
#     print("Transaction Success")
# else:
#     print("Transaction failed")

#task3
# mark=int(input("Enter your mark: "))
# if mark>=35:
#     print("You have passed the exam.")
# else:  
#     print("You have failed the exam.")

#task4
# actual_password = "python123"
# password = input("Enter your password: ")
# if password == actual_password:
#     print("Login successful")   
# else:
#     print("Incorrect password")


#task5
# balance = 5000
# amount = int(input("Enter the amount to withdraw: "))
# if amount <= balance:
#     balance -= amount
#     print("Withdrawal successful. Remaining balance:", balance)
# else:
#     print("Insufficient balance. Withdrawal failed.")

#elif
#task 1
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# elif marks >= 35:
#     print("Grade: D")
# else:
#     print("Grade: F")

#task 2
# income=int(input("Enter your income: "))
# if income>1000000:
#     print("Tax Rate: 30%")
# elif income>500000:
#     print("Tax Rate: 20%")
# elif income>200000:
#     print("Tax Rate: 10%")
# else:
#     print("no tax")

#match case
#task 1
# date=int(input("Enter the date (in format DD): "))
# if(date<0 ):
#     print("Invalid date")
# else:
#     date=date%7
#     match date:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")
#         case 0:
#             print("Sunday")
#         case _:
#             print("Invalid date")

#challenge
actual_username = "admin"
actual_password = "admin123"
username=input("Enter your username: ")
password=input("Enter your password: ")

if username == actual_username and password == actual_password:
    print("Login successful")

    print("Menu")

    
else:
    print("Incorrect username or password")
