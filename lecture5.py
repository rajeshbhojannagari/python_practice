# class Student:
#     name="Rajesh"
#     grade="A"
# student1=Student()
# print(student1.name)
# print(student1.grade)

# class Student:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
# Student1=Student("TATA","High",2025)
# print(Student1.brand)
# print(Student1.model)
# print(Student1.year)

# class Bank:
#     def __init__(self,bankAcc,branch,withdraw):
#         self.bankAcc=bankAcc
#         self.branch=branch
#         self.withdraw=withdraw
#     def bankDet(self):
#         print(f"You have Account in {self.bankAcc} and branch is {self.branch} and the money withdraw is {self.withdraw}")
# state=Bank("ICICI","Hyderabad",500)
# state.bankDet()

# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def Sum(self):
#         sum=self.num1+self.num2
#         print("Sum is ",sum)
#     def Sub(self):
#         sub=self.num1-self.num2
#         print("Sub is ",sub)
#     def Mul(self):
#         mul=self.num1*self.num2
#         print("Mul is ",mul)
#     def Div(self):
#         div=self.num1/self.num2
#         print(f"Div is {div:.2f}")
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# calc=Calculator(a,b)
# calc.Sum()
# calc.Sub()
# calc.Mul()
# calc.Div()


# class Employee:
#     def __init__(self,EmpId,EmpName,EmpSal):
#         self.EmpId=EmpId
#         self.EmpName=EmpName
#         self.EmpSal=EmpSal
#     def annual(self):
#         print(f"Employee Name: {self.EmpName}-ID: {self.EmpId} Annual salary: {12*self.EmpSal}")
# emp=Employee(1,"Rajesh",100000)
# emp.annual()

class Employee:
    def __init__(self,EmpId,EmpName,EmpSal,EmpDay,Exp):
        self.EmpId=EmpId
        self.EmpName=EmpName
        self.EmpSal=EmpSal
        self.EmpDay=EmpDay
        self.Exp=Exp
    def annual(self):
        print(f"Employee Name: {self.EmpName}   ID: {self.EmpId}     Annual salary: {12*self.EmpSal}")
        sal=self.EmpSal*self.EmpDay/30
        print(f"{sal:.2f}")
        if(self.EmpSal>=10000 and self.Exp>=3):
            print("Eligible for Bonus")
        else:
            print("Not Eligible for Bonus")
emp=Employee(1,"Rajesh",100000,25,2)
emp.annual()