# Question 1
# class Employee:
#     emp_name = "Sonu"
#     emp_id = 783
#     salary = 1000

# p1 = Employee()
# print("name is :" ,p1.emp_name)
# print("id is:" ,p1.emp_id)
# print("salary:" , p1.salary)

## Question 2
# class Calculator:
#     def addition(self,a,b):
#         return a+b
#     def subtraction(self,a,b):
#         return a-b
#     def multiply(self,a,b):
#         return a*b
#     def division(self,a,b):
#         return a/b
    
# c = Calculator()
# print(c.addition(2,3))
# print(c.subtraction(2,3))
# print(c.multiply(2,3))
# print(c.division(2,3))    

###Question 3
# class Book:
#     def  __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display_details(self):
#         print(f"{self.title}, {self.author} ,{self.price}")

# b = Book("ON THE SAVAGE SIDE ","Tiffany" , 900)
# b.display_details()        
        
####Question 4
# class Vehicle:
#     def display(self):
#         print("I have a vechile")

# class Car(Vehicle):
#     def display(self):
        
#         print("i have a Car")
#         super().display()


# c = Car()
# c.display()        



#####Question 5
# import re
# txt = "Python123Assigment456" 
# x = re.findall("\d",txt) 
# print(x)                          
               