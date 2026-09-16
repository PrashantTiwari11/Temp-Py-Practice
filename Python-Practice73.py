# 67_oop_practical_projects.py
# OOP - 10 practical programs/features

class Student:
    def __init__(self,name,marks):self.name,self.marks=name,marks
    def average(self):return sum(self.marks)/len(self.marks)
    def result(self):return 'Pass' if self.average()>=40 else 'Fail'
class BankAccount:
    def __init__(self,owner,balance=0):self.owner,self.balance=owner,balance
    def deposit(self,x):self.balance+=x
    def withdraw(self,x):
        if x<=self.balance:self.balance-=x;return True
        return False
class Rectangle:
    def __init__(self,l,w):self.l,self.w=l,w
    def area(self):return self.l*self.w
    def perimeter(self):return 2*(self.l+self.w)
class Animal:
    def speak(self):return 'Animal sound'
class Dog(Animal):
    def speak(self):return 'Bark'
class Employee:
    company='Tech Company'
    def __init__(self,name,salary):self.name,self.salary=name,salary
    def yearly_salary(self):return self.salary*12
s=Student('Prashant',[75,82,68]);print('1. Student:',s.name)
print('2. Average:',s.average());print('3. Result:',s.result())
a=BankAccount('Aman',1000);a.deposit(500);print('4. Deposit balance:',a.balance)
print('5. Withdrawal:',a.withdraw(300),a.balance)
r=Rectangle(10,5);print('6. Area:',r.area());print('7. Perimeter:',r.perimeter())
print('8. Inheritance:',Dog().speak())
e=Employee('Riya',30000);print('9. Class variable:',e.company);print('10. Yearly salary:',e.yearly_salary())
