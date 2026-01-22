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
number=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{number}* {i} =",number*i)
    