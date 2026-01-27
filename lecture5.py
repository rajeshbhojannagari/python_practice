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

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def Sum(self):
        sum=self.num1+self.num2
        print("Sum is ",sum)
    def Sub(self):
        sub=self.num1-self.num2
        print("Sub is ",sub)
    def Mul(self):
        mul=self.num1*self.num2
        print("Mul is ",mul)
    def Div(self):
        div=self.num1/self.num2
        print(f"Div is {div:.2f}")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
calc=Calculator(a,b)
calc.Sum()
calc.Sub()
calc.Mul()
calc.Div()

