# student_grades={
#     "Alice":"A",
#     "Age":20,
#     "Grade":"A",
#     "Subject":"CSE"
# }
# print(student_grades)
# Color_Fruit={
#     "Mango":"Yellow",
#     "Grapes":"Green",
#     "Apple":"Red",
#     "Banana":"Yellow"
# }
# print(Color_Fruit.keys())
# print(Color_Fruit.values())

# name=dict(Varanasi="Mahesh babu",Sprit="Prabhas",AA22="Allu Arjun",Dragon="NTR")
# print(name.keys())
# print(name.values())
# print(name.get("Varanasi"))
# students={'Rajesh':87,'Shyam':85,'Gopal':89}
# key=input()
# if key in students:
#     print(students[key])
# else:
#     print("not found")

# Details={'name':'Rajesh','age':20,'City':'Hyderabad'}
# print(Details)
# del Details['age']
# print(Details)
# print(len(Details))
# print('name' in Details)
# for i in Details:
#     print(i,Details[i])
# print(len(Details))

# data={
#     'id':101,
#     'info':{
#         'name':'Alice',
#         'age':20
#     }
# }
# print(data['info']['name'])
# print(len(data))
# print(data.items())

# data={'a':1,'b':2,'c':3}
# for i in list(data.keys()):
#     if(data[i]%2==0):
#         del data[i]
# print(data)

# a={'a':1,'b':9}
# b={'b':2,'a':8}
# t=a|b
# print(t)



# import copy
# student={
#     'name':'Rajesh',
#     'marks':[87,80,78]
# }
# another_Student1=copy.deepcopy(student)
# student['marks'].append(99)
# print(student)
# print(another_Student1)

# def function():
#     print("Hello World")
#     return "Retured output"
# function()
# function()
#print(function())

# def fun(first_name,last_name,country):
#     print("Hey Buddy")
#     print(f"My name is {first_name} {last_name}")
#     print(f"I live in {country}")
# fun("Rajesh","Bhojannagari","India")

# def sum(a,b):
#     Sum=a+b
#     print(Sum)
# sum(5,6)

# def cal(a,b):
#     sum=a+b
#     print("Sum= ",sum)
#     print("a**2= ",a**2)
#     print("b**2= ",b**2)
#     print("Square of sum= ",sum**2)
# cal(a=int(input("Enter a: ")),b=int(input("Enter b: ")))

# def div(a,b):
#     divide=a/b
#     print(f"{divide:.2f}")
# div(5,6)

# def sum(a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     print(sum)
# a=[1,2,3,4,5,6,7,8,9,10]
# sum(a)

# def fun(first_name,last_name,country="India"):
#     print("Hey Buddy")
#     print(f"My name is {first_name} {last_name}")
#     print(f"I live in {country}")
# fun("Rajesh","Bhojannagari","UK")

# import random
# a=int(input("Enter Number a: "))
# b=int(input("Enter Number b: "))
# number=random.randint(a,b)
# print(number)
# guessNumber=int(input("Guess number: "))
# while True:
#     if(guessNumber==number):
#         print("You Guessed It right")
#         break
#     else:
#         guessNumber=int(input("Guess number: "))

