# password="vikram"
# while True:
#     enter=input("Guess a password: ")
#     if(enter==password):
#         print("You have entered password right")
#         break
#     else:
#         print("Try Again")

# amount=int(input("Enter the amount you want to withdraw  500 and 200 notes are available: "))
# if amount>=200 and amount%100==0 and amount!=300:
#     print("Discharging cash")
# else:
#     print("Denomination not available")

# time1=int(input("Enter a hour in 24 hrs format: "))
# while True:
#     if (time1>=0 and time1<12):
#         print("AM")
#         break
#     elif(time1>=12 and time1<24):
#         print("PM")
#         break
#     else:
#         time1=int(input("Enter a hour in 24 hrs format: "))  
        
#Multiplication
# number=int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{number}* {i} =",number*i)

# name='''Hey Buddy
# My Name is Rajesh
# I am from 
# Hyderabad'''
# print(name)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     i=i+1
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     i=i+1
#     print()


# for i in range(6,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

# for i in range(6,0,-1):
#     print("*"*i)

# for i in range(6,0,-1):
#     for j in range(i,0,-1):
#         print("*", end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     i=i+1
#     print()

# list1=[1,2,3,4,5]
# list1.append(6)
# list1.insert(3,7)
# list1.pop()
# print(list1)

# name="121"
# name1=name[::-1]
# if(name==name1):
#     print("Palindrome")
# else:
#     print("no")

# number=int(input("Enter a number: "))
# for i in range(2,number+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i," ")