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

#