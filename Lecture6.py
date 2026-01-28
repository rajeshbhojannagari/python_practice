# def num(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(num(1,23,8,45,8))

# def names(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
# (names(name="Rajesh",age=20,college="LPU"))

# def values(msg,*args,**kwargs):
#     print(msg)
#     print(args)
#     print(kwargs)
# values(("Hey Buddy"),1,2,33,4,name="Rajesh",age=20,city="Hyderabad")

# def sq(x):
#     return x**x
# print(sq(2))

# y=lambda x:x**2
# print(y(5))


# y=lambda a,b:(a+b)
# print(y(5,3))

# a=int(input("a: "))
# b=int(input("b: "))
# y=lambda a,b: a if(a>b) else  b
# print(y(a,b))


# list1=[1,2,3,4,5,6,7,8]
# res=[]
# for i in list1:
#     res.append(i*i)
# print(res)
# z=list(map(lambda x: x**2,list1))
# print(z)

# from functools import reduce
# a=reduce(lambda x,y:x+y,list1)
# print()
# print(a)



# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name=name
#         self.grade=grade
#         self.percentage=percentage
#     def student_details(self):
#         print(f"{self.name} is in class {self.grade} with {self.percentage}%")
#     def get_percent(self):
#         return self.percentage
# student1=Student("Rajesh",10,94)
# student2=Student('Vikram',10,92)
# student1.student_details()
# student2.student_details()
# print(student1.get_percent())
# print(student2.get_percent())

# class Bank:
#     def __init__(self,Balance,withdraw,deposit):
#         self.Balance=Balance
#         self.withdraw=withdraw
#         self.deposit=deposit
#     def details(self):
#         print(f"deposit amount is {self.deposit} and balance is {self.Balance + self.deposit}")
#     def withd(self):
#         print(f"withdraw amount is {self.withdraw} and balance is {self.Balance-self.withdraw}")

# per1=Bank(20000,1200,1000)
# per1.details()
# per1.withd()


# class Bank:
#     def __init__(self,Balance,withdraw,deposit):
#         self.__Balance=Balance
#         self.withdraw=withdraw
#         self.deposit=deposit
#     def depo(self):
#         self.__Balance=self.__Balance+self.deposit
#         print(f"Balance is {self.__Balance}")
#     def withd(self):
#         if(self.withdraw>self.__Balance):
#             print("Insufficeint balance")
#         else:
#             self.__Balance=self.__Balance-self.withdraw
#             print(f"Balance is {self.__Balance}")
# per1=Bank(10000,1200,2000)
# per1.depo()
# per1.withd()


# class Bank:
#     def __init__(self,Balance):
#         self.__Balance=Balance
#     def Deposit(self,deposit):
#         self.__Balance+=deposit
#         print(f"Balance is {self.__Balance}")
#     def Withdraw(self,withdraw):
#         if(withdraw>self.__Balance):
#             print("Insufficeint Balance")
#         else:
#             self.__Balance-=withdraw
#             print(f"Balance is : {self.__Balance}")
# per1=Bank(20000)
# per1.Deposit(5000)
# per1.Withdraw(2000)

# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name=name
#         self.grade=grade
#         self.percentage=percentage
#     def stu_det(self):
#         print(f"{self.name} is in class {self.grade} with percentage {self.percentage}%")
# #student1=Student("Rajesh",12,94)
# class GraduateStudent(Student):
#     def __init__(self, name, grade, percentage,stream):
#         super().__init__(name, grade, percentage)
#         self.stream=stream
#     def upt_det(self):
#         print(f"{self.name} is in class {self.grade} with percentage {self.percentage}% and stream is {self.stream}")
# Grad_student1=GraduateStudent("Rajesh",12,94,"CSE")
# Grad_student1.upt_det()

# class details:
#     def __init__(self,studentname,regno,year):
#         self.studentname=studentname
#         self.regno=regno
#         self.year=year
# class mentor(details):
#     def __init__(self,studentname,regno,year,mentorname):
#         super().__init__(studentname,regno,year)
#         self.mentorname=mentorname
#     def printdet(self):
#         print(f"Student name is {self.studentname} and mentor name is {self.mentorname}")
# std1=mentor("rajesh",12313848,3,"Manpreet senghal")
# std1.printdet()

# class Employee:
#     def details(self):
#         return ("No details available")
# class Payment1(Employee):
#     def details(self):
#         return "Payment amount is 5000"
# class Payment2(Employee):
#     def details(self):
#         return "Payment amount is 8000"
# def payment(Employee):
#     print(Employee.details())

# pay1= Payment1()
# pay2=Payment2()
# payment(pay1)
# payment(pay2) 