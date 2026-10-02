# #int 
# age = 20
# print(type(age))

# #float
# weight = 63.7
# print(type(weight))

# #complex
# com = 2+3j
# print(type(com))

# #string
# name = "Bhawani"
# print(len(name))
# print(type(name))

# #list
# list = [7,31,25,1]
# print(len(list))
# print(type(list))

# #dictionary
# dict = {'name':'chintu','age':'21','city':'Jaipur'}
# print(len(dict))
# print(type(dict))

# #tuple
# tup=(1,2,3,4)
# print(len(tup))
# print(type(tup))

# #set 
# set={1,2,3,4,5,6,7,9,0}
# print(len(set))
# print(type(set))

# #none
# roll_no=None
# print(type(roll_no))

# #range
# num = range(1,5)
# for i in num:
#     print(i)


# a = int(input("enter a first number:"))
# b = int(input("enter second number"))
# print(a+b)

# a=20
# b=12
# c=30
# print(a,b,c)
# a,b,c=c,a,b
# print(a,b,c)

# a="Shruti"
# b=20
# print(f"{a} {b}")

####################Day 2###############

# n= int(input("enter your number"))
# for i in range(1,11):
#     print(n,'x',i,'=', n*i )

# a = "shruti"
# b  = 20
# print (a+ " " + str(b)) 
# 
# 
# n = ["Divya","apple","juice"]
# x,y,z=n
# print(x)
# print(y)
# print(z) 

# n = ("Divya","apple","juice")
# x,y,z=n
# print(x)
# print(y)
# print(z) 

# n ="ABC"
# x,y,z=n
# print(x)
# print(y)
# print(z) 

# _ = 10
# print(_)
 
# x = "Sonu"
# y = "is"
# z = "great"
# print(x+y+z)

# x = 5
# y = "Bhawani"
# print(x,y)
# print(type(x))

# txt = "The best things in life are free"
# print("sonu" not in txt)
# if "bhawani" in txt:
#     print("yes , bhawani is present.")
# elif "sonu" in txt:
#     print("yes, sonu is present")  
# else:
#     print ("NO, not present")      

################################################################# Slicing and indexing #######################################################



# b= "Hello, World!"
# print(b[-4:-1])

# print(b.upper())
# print(b.strip())
 
# print(b.replace("o","_",1))
# print(b.split("W"))

# age = 21
# txt = f"My name is sonu, I am {age:.5f}"
# print(txt)

# s = 'Converts the first \"character" to upper case'
# print(s)
  
# for _ in range(1,6):
#  print(_) 

# a = "i am sonu rao"
# print(a.capitalize())
# print(a.count('m'))


# print(ord('A'))
# print(chr(98))

# x = 2
# y = 5
# print(x**y)

# a = 5;
# b = 2;
# a = a +b ;
# b = a - b ;
# a = a - b ;
# print(a)
# print(b)

#################################################################### LIST ################################################################

# list1 =[10,20,30,40,50]
# print(list1[0])


# list1 = [1,"banana",True]
# list2 = [1,2,4,7,9]
# list3 = [True,False,False]

# print(list1[-1])
# print(list1[1:4])
# print(list[-5:2])

a = ["apple","banana","grapes"]
b = ["mango","dragonfruit", "kiwi"]
# a[1:3]= ["cherry"]
# print(a)

# a.append("orange")
# print(a)

# a.insert(1,"orange")
# print(a)

# a.extend(b)
# print(a)

# a.remove("grapes")
# print(a)

# a.pop(1)
# print(a)

# a.clear()
# print(a)

# a.delete()
# print(a)


############################################################################ loops ###################################################################

# a = ["apple","banana","cherry"]
# for x in a:
#     print(x)


# a = ["apple","banana","cherry"]
# for i in range(len(a)):
#     print(a[i])

# a = ["apple","banana","cherry"]
# i = 0
# while i < len(a):
#     print(a[i])
#     i = i+1


####################List comprehension################

# fruits = ["apple","banana","kiwi","cherry","mango"]
# print([x for x in fruits])
# print([x for x in fruits if "a" in x])
#newlist = [x for x in fruits if x != "apple"]
# print(newlist)

# newlist = [x for x in range(10) if x<5]
# print(newlist)

# newlist = [x.upper() for x in fruits]
# print(newlist)

# newlist = ['hello' for x in fruits]
# print(newlist)

# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# n = [4,2,8,7,6]
# n.sort()
# print(n)
# n.sort(reverse=True)
# print(n)
# fruits.sort(reverse=True)
# print(fruits)

# fruits.reverse()
# print(fruits)

# fruits = ["Apple", "Banana","Kiwi","Cherry","Mango"]
# b = fruits[:]
# print(b)

# list1 = ["a","b","c"]
# list2 = [1,2,3]
# list3 = list1 + list2
# print(list3)

# list3 = list1.count('a')
# print(list3)

# a = ['a', 'b', 'c']
# print(a.index('a'))

# colour = ["red", "blue", "purple"]
# colour.remove("red")
# print(colour)
# colour.pop(1)
# print(colour)

# a = [1,2,3,4,5]
# print(max(a))
# print(min(a))


############################################# 11 june #########################################################################
# a=("apple","banana")
# print(a)

# this = ("apple",)
# this1= ("apple")
# print(type(this))
# print(type(this1))

# a = ("abc",23,True,"male",40)

# b = ("apple","banana","cherry")
# if "apple" in b:
#     print("yes, apple is a fruit")

# y = list(b)
# y[1] = "kiwi"
# print(y)
# x = tuple(y)
# print(x)

# b = ("apple","banana","cherry")
# y = list(b)
# y.append("orange")
# print(y)
# x = tuple(y)
# print(x)
# b = ("apple","banana","cherry")
# # y = ("orange","mango","kiwi")
# # b+=y
# # print(b)

# del b 
# print(b)b

# b = ("apple","banana","cherry")
# x,y,z=b
# print(x)
# print(y)
# print(z)

# fruits = ("apple","banana","cherry","strawberry","raspberry")
# (green,*yellow,red)= fruits
# print(green)
# print(yellow)
# print(red)

# b = ("apple","banana","cherry")
# for i in range(len(b)):
#     print(b[i])

# b = ("apple","banana","cherry")
# c = b*2
# print(c)

##################################SETS#########################

# myset = {"apple","banana","cherry"}

# myset = {"apple","banana","cherry"}
# myset.add("orange")
# print(myset)

# a = {"apple","banana","cherry"}
# b = {"pineapple","mango","papaya"}
# a.update(b)
# print(a)

# a = {"apple","banana","cherry"}
# b = ["a","b","c"]
# a.update(b)
# print(a)

# a = {"apple","banana","cherry"}
# a.discard("banana")
# a.remove("banana")

# a = {"apple","banana","cherry"}
# x = a.pop()
# print(x)
# print(a)

##################   SET OPERATIONS   #####################

# set1 ={"a" , "b", "c"}
# set2 = {1,2,3}
# set3 = set1.union(set2)
# set3 = set1 |set2
# print(set3)

# set1 ={"a" , "b", "c"}
# set2 = {1,2,3}
# set3 = {"john", "elena"}
# set4 = {"apple","banana","cherry"}
# myset = set1.union(set2,set3,set4)
# print(myset)

# myset = set1 | set2 | set3 | set4
# print(myset)

# set1 = {"apple", "banana" ,"cherry"}
# set2 = {"google","microdoft","apple"}
# set3 = set1.intersection(set2)
# print(set3)
# set3 = set1 & set2
# print(set3)

# set1 = {"apple", "banana" ,"cherry"}
# set2 = {"google","microdoft","apple"}
# set1.intersection_update(set2)
# print(set1)

# set1 = {"apple", "banana" ,"cherry"}
# set2 = {"google","microdoft","apple"}
# set3 = set1.difference(set2)
# print(set3)


# set1 = {"apple", "banana" ,"cherry"}
# set2 = {"google","microdoft","apple"}
# set1.difference_update(set2)
# print(set1)

# set1 = {"apple", "banana" ,"cherry"}
# set2 = {"google","microdoft","apple"}
# set3 = set1.symmetric_difference(set2)
# set4 = set1 ^ set2
# print(set3)
# print(set4)

###############################################################12 june#############################################################################
#########################################################dictionary####################################################
# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 2004,
#     "colour": "yellow"

# }
# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in thisdict dictnory")
# x = thisdict.setdefault("colour","red")
# print(thisdict)

# print(thisdict["brand"])
# print(len(thisdict))

# thisdict = {
#     "brand": "ford",
#     "electric": "false",
#     "year": 2004,
#     "colours": ["red","white","blue"]

# }
# print(type(thisdict))

# a = dict(name="john", age =36,country ="norway")
# print(a)

# car = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 2004,
#     "colour": "yellow"

# }
# x = car.get("model")
# print(x)

# x = car.keys()
# print(x)

# car["colour"] ="white"
# print(car)

# x = car.values()
# print(x)

# thisdict = {
#     "brand": "ford",
#     "model": "mustang",
#     "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# thisdict.popitem()
# print(thisdict)
# thisdict.clear()
# print(thisdict)

# for x in thisdict.values():
#     print(x)

# for x in thisdict.keys():
#     print(x)

# for x in thisdict.items():
#     print(x,y)  
  
# myfamily = {
#     "child1" : {
#         "name" : "vishnu",
#         "year" : 2004
#  },
#  "child2" : {
#         "name" : "yogesh",
#         "year" : 2007
#  },
#  "child1" : {
#         "name" : "om",
#         "year" : 2011
#  },
# }
# # print(myfamily)
# # print(myfamily["child2"]["name"])

# for x, obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y + ":", obj[y])

# mydict = {
#     "english" : 81,
#     "maths" : 99,
#     "science" : 97
# }

# mydict["social"]= 98
# print(mydict)

# mydict.update({"english": 95})
# print(mydict)


###############################conditional Statements###################
# x = int(input("enter your input:"))
# if x == 1:
#  print("Sunday")
# elif x == 2:
#  print("Monday")
# elif x == 3:
#  print("Tuesday") 
# elif x == 4:
#  print("Wednesday") 
# elif x == 5:
#  print("Thrusday") 
# elif x == 6:
#  print("friday") 
# elif x == 7:
#  print("saturday")  
# else :
#  print("oops wrong input")

# a = 33
# b = 200
# if b > a:
#     print("b is greater than a")

########################loops#############################

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
  
  
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
  
  
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)


# for x in range(2, 30, 3):
#     pass




#######################Day3 ####################################
# r = range(10)
# print(r[2])
# print(r[:3])

# r = range(0,10,2)
# print(6 in r)
# print( 7 in r)

# print (len(r))

##############################Functions#########################################

# def c_to_k(celsius):
#     return (celsius+273)
# print(c_to_k(77))

# temp1 = 77
# celsius1 = (temp1-32)*5/9
# print(celsius1)
 # we have to print again n again the same code so 

# def f_to_c(farh):
#     return(farh-32)*5/9
# print(f_to_c(77))

# def get_greeting():
#     return "Hello from a function"
# message = get_greeting()
# print(message)

# def fun(fname):
#     print(fname + " hello student")
# fun("sonu")
# fun("bhawani")    

# def fun(fname="bhawani" , lname="singh"):
#     print(fname+ " "+lname + " hello student")
# fun()

# def my_function(animal,name):
#     print("i have a",animal)
#     print("my" , animal + "'s name is ", name)
# my_function(name ="Buddy", animal="dog")    

# def my_fun(fruits):
#     for i in fruits:
#         print(i)
# my_fruits = ["apple","banana","cherry"]
# my_fun(my_fruits) 

# def my_func(person):
#     print("name:",person["name"])
#     print("age:",person["age"])
# my_person = {"name": "Sonu","age":21} 
# my_func(my_person)
# 
# def my_func(x,y):
#     return x+y
# result = my_func(5,3)
# print(result)   

# def my_func():
#     return["apple","banana","cherry"]
# fruits = my_func()
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# def my_func():
#     return(10,20)
# x,y=my_func()
# print("x:", x)
# print("y:", y) 

##################################*args and **kargs#########################

# def my_func(*kids):
#     print("the youngest child is" + kids[2])
# my_func("Emily","kitty", "serena") 
# 
# def func(greeting ,*args):
#     print("Type:",type(args))
#     print("First argumengt:", args[0])
#     print("Second argument:",args[1])
#     print("All arguments:",args)

#     for name in args:
#         print(greeting,name)

# func("hello","chintu","mintu","hintu")


# def func(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(func(1,2,3))
# print(func(10,20,30,40))
# print(func(6))

# def func(**myvar):
#     print("Type:", type(myvar))
#     print("Name:"+ myvar["name"])
#     print("age:", myvar["age"])
#     print("All data:", myvar)
# func(name="sonu",age = 20,city = "jaipur")    


# def func(username, **details):
#     print("Username:",username)
#     print("Additinal details:")
#     for key,value in details.items():
#         print(" ",key + ":" , value)
# func("Emily",age = 25,city= "oslo", hobby = "coding")        

# def my_func(title,*args,**kwargs):
#     print("Title:",title)
#     print("Positional arguments:",args)
#     print("Keyword arguments:", kwargs)
# my_func("User Info", "Bhawani","Sonu", age = 25, city = "Jaipur")    




############################################################################ 15 june #####################

############################ Decorators #########################
# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# def addgreeting(func):
#     def myinner():
#         return "Hello " + func() + " Have a good day!"
#     return myinner

# @changecase
# @addgreeting
# def myfunction():
#     return "Chintu"

# print(myfunction())


############################################################################## OOPs ###############################################################################
 
# class MyClass:
#     x = 5

# p1=MyClass()
# print(p1.x)
# del p1
# print(p1.x)

# p1 = MyClass()
# p2 = MyClass()
# p3 = MyClass()

# print(p1.x)
# print(p2.x)
# print(p3.x)

# class Base:
#     pass


############################# Constructors ###########################

# class Person:
#     def __init__(self,name="Sonu",age = 20):
#         self.name=name
#         self.age=age
# p1=Person() 
# print(p1.name)
# print(p1.age)       
# p1.age = 26 ###for update
# print(p1.age)
# del p1.age

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year},{self.brand},{self.model}")

# car1 = Car("Toyota","Corolla","2020")
# car1.display_info()        

# class Person:
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         return "Hello, "  + self.name

#     def welcome(self):
#         message = self.greet()
#         print(message+ " !you are welcome") 

# p1=Person("chintu")
# p1.welcome()         

# class Calculator:
#     def add(self ,a,b):
#         return a+b
#     def multiply(self,a,b):
#         return a*b
# calc = Calculator()
# print(calc.add(5,3))
# print(calc.multiply(4,7))

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
#     def __str__(self):
#       return f"{self.name} {self.age}"  
# p1 = Person("Lala",36)
# print(p1)  

class Playlist:
   def __init__(self,name):
      self.name = name
      self.songs=[]

   def add_song(self, song):
        self.songs.append(song)
        print(f"Address: {song}")

   def remove_song(self,song):
       if song in self.songs: 
         self.songs.remove(song)
         print(f"Removed: {song}")

   def show_songs(self):
      print(f"Playlist '{self.name}' :")
      for song in self.songs:
         print(f" - {song}")

my_playlist = Playlist("Favourites")
my_playlist.add_song("Song A") 
my_playlist.add_song("Song B")
my_playlist.add_song("Song C") 
my_playlist.show_songs()  

my_playlist.remove_song("Song B")
my_playlist.show_songs() 

# del Playlist.remove_song
# my_playlist.remove_song("Song A")



##########################   Inheritance  ###################################

# ########################## Single inheritance ############
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking")
# my_dog = Dog()
# my_dog.bark()
# my_dog.eat()   
# 
# class Person:
#     def __init__(self,name):
#         self.name = name
# class Student(Person):
#     def display(self):
#         print("Name:" , self.name)

# s = Student("Chintu")
# s.display()      
# 
############################ Single In heritance ################
#
# class Animal:
#     pass
# class Dog(Animal):
#     pass

############################ Multiple inheritance ##################

# class Father:
#     def skills(self):
#         print("Driving")

# class Mother:
#     def skills2(self):
#         print("Cooking")

# class Child(Father,Mother):
#     pass

# c = Child()
# c.skills()
# c.skills2()


############################ Multilevel Inheritance #################

# class Grandparent:
#     def house(self):
#         print("Grandparent's House")

# class Parent(Grandparent):
#     pass

# class Child(Parent):
#     pass

# c = Child()
# c.house()

############################## Hierarchical Inheritance ###################

# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     pass        

# class Cat(Animal):
#     pass  

# d = Dog()
# d.eat()
# c = Cat()
# c.eat()


############################## Hybrid Inheritance ###################
    #    A
    #   / \
    #  B   C
    #  \   /
    #    D

# class A:
#     def displayA(self):
#         print("Class A")

# class B(A):
#     def displayB(self):
#         print("Class B") 

# class C(A):
#     def displayC(self):
#         print("Class C")

# class D(B,C):
#     def displayD(self):
#         print("Class D")

# obj = D()
# obj.displayA()  
# obj.displayB()
# obj.displayC()
# obj.displayD()                             

##EXAMPLE

# class Person():
#     def display(self):
#         print("I am Person")

# class Student(Person):
#     def displayS(self):
#         print("i am student") 

# class Employee(Person):
#     def displayE(self):
#         print("i am employee")

# class Intern(Student,Employee):
#     def displayI(self):
#         print("I am intern")

# obj = Intern()
# obj.display() 
# obj.displayS() 
# obj.displayE() 
# obj.displayI()        

############################################### Polymorphism #######################

# def add (a,b):
#  return a+b
# def add (a,b,c):
#  return a+b+c


# # print(add(1,2))
# print(add(1,2,3))

# class Calculator:
#     def add(self,a,b,c=0):
#         return a+b+c

# obj = Calculator()
# print(obj.add(1,2))
# print(obj.add(1,2,3))

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):        
#         print("Dog Barks")

# obj = Dog()
# obj.sound()        


# class Animal:
#     def sound(self):
#          print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self): 
#         super().sound()       
#         print("Dog Barks")

# obj = Dog()
# obj.sound()

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("person constructor is called")

# class Student(Person):
#     def __init__(self,name,course):
#         super().__init__(name)  ##Calls parent Constructor
#         self.course = course
#         print("student constructor is called")

# s = Student("Chintu", "CSE")
# print(s.name)    #Inherited from person
# print(s.course)  #Student's own attribute  
# 
# 
###################################Tasks################
# 
# class Vechile:
#     def start():
#         print("Vechile is starting")

# class Car(Vechile):
#     def start(self):
#         print("Car starts")

# class Bike(Vechile):
#     def start(self):
#         print("Bike starts")

# obj1 = Car()
# obj2 = Bike()
# obj1.start()
# obj2.start()



# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         print("bonus")

# class Manager(Employee): 
#     def calculate_bonus(self):
#         return self.salary*20/100

# class Developer(Employee): 
#     def calculate_bonus(self):
#         return self.salary*10/100         

# obj1 = Manager("Sonu", 100000)
# print(obj1.name)
# print(obj1.calculate_bonus())

# obj2 = Developer("Chintu", 100000)
# print(obj2.name)
# print(obj2.calculate_bonus())



# class Shape:
#     def area():
#         pass

# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#     def area(self):
#         print("Area of rectangle is:" , self.l*self.b)

# class Circle(Shape):
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         print("Area of Circle is:" , 3.14* self.r*self.r)        

# class Triangle(Shape):
#     def __init__(self,b,h):
#         self.b = b
#         self.h = h
#     def area(self):
#         print("Area of Triangle is:" , 1/2*self.b*self.h)

# obj1 = Triangle(10,20)
# obj1.area()

# obj2 = Circle(2)
# obj2.area()

# obj3 = Rectangle(10,20)
# obj3.area()


######################################################################## 18 june #########################################################
################################# Exception Handling #####################

# try:
#     print(x)
# except:
#     print("x is not defined")

# x = 10
# try:
#     print(x)
# except NameError:
#     print("x is not defined")
# except:
#     print("something went wrong")        


# try:
#     print("hello")
# except:
#     print("something went wrong")
# else:
#     print("nothing went wrong")

# try:
#     print(x)
# except:
#     print("something went wrong")
# finally:
#     print("the 'try except' is finished")        

# x = -1
# if x < 0:
#     raise Exception("Sorry no numbers below zero")

# x = "hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")



# try:
#     num1 = int(input("Enter number 1"))
#     num2 = int(input("Enter number 2"))

#     result = num1/num2
#     print("Result =" , result)

# except ZeroDivisionError :
#     print("error: division by zero is not allowed")

#########################################################Modules######################

# import Module as mmd
# Module.greeting("Chintu")

# a = mmd.person1["age"]
# print(a)

# from Module import person1
# print(person1["age"])

# import datetime
# x=datetime.datetime.now()
# print(x)

# arr = [10,5,20,8,15]
# print("Minimum :" ,min(arr))
# print("Maximun" , max(arr))

# x = -5
# print(abs(x))

# x = 2
# y = 5
# print(pow (x,y))

# import math
# x=math.sqrt(64)

# x=math.ceil(2.17)
# y=math.floor(2.17)
# print(x)
# print(y)

# x = math.pi
# print(x)


# x = math.pi
# r = int(input("Enter radius:"))

# print("area :" , x*r*r )
# print("circumference:" ,2*x*r)
# print("Rounded area:", math.ceil(x*r*r))

# import re ##regular expression that is used to perform operation on strings
## ^ starting
## .* bich ki values
## $ end value

# txt = "we are good students os Upflaiers"
# x = re.search("^we.*Upflaiers$",txt)
# if x:
#     print("YES! we have a match")
# else:
#     print("No match")    

# y = re.findall("o",txt)
# print(y)

# \s --> spaces or tabs ki baat krrhe h

# import re
# txt = "The rain in spain"
# x = re.search("\s",txt)
# print("The first white space chracter is located in position:", x.start())

# import re
# txt = "The rain in spain"
# x = re.split("\s",txt)
# print(x)

# import re
# txt = "The rain in spain"
# x = re.split("\s",txt, 1)
# print(x)

# import re
# txt = "The rain in spain"
# x = re.sub("\s","oo",txt,2) ##2 position tk space ki jagah oo
# print(x)

########################################## File Handling ##########################################

f = open("demofile.txt")
# print(f.read())

# print(f.readline())
# print(f.readline())
# print(f.readline())