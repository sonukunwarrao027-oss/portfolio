##Question 1
a = int(input("Enter your number"))
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print(a,"is not prime")
#             break      
#     else:
#         print(a,"is prime")
# else:
#     (a,"is not prime")

factors = [i for i in range(2,a) if a%i==0]
if len(factors)==0 and a>1:
    print(a,"is prime")
else:
    print(a,"is not prime")    
                  






######Question 2
# a = 100
# b = 100

# x = [1,2,3]
# y = [1,2,3]

# print(a==b)
# print(a is b)
# print(x==y)
# print(x is y)

####3Question 3
# a =[1,2,-1,0,5]
# print([x for x in a if x>0])

####Question 4
# list = [x**2 for x in range (1,21) if x%2 == 0 and x%5 ==0]
# print(list)

#############Question 5
# list = [1,2,3,4,5,6]
# print(min(list))
# print(max(list))

