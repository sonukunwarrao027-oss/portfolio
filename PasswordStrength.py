password = input("Enter your password: ")
length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False
score = 0
for ch in password:
    
    
        if ch.isupper() :
           has_upper=True
           
        elif ch.islower():
           has_lower = True
        elif ch.isdigit():
           has_digit = True
        else:
           has_special = True
           
if length>=8:
    score +=1

if has_upper:
    score +=1
    
if has_lower:
    score +=1    

if has_digit:
    score +=1 
    
if has_special:
    score +=1   
    
if score<=2:
   print("Weak password")
   print("Suggestions:")
   if length<8:
       print("make the password of atleast 8 characters")
   if not has_upper:
        print("add atleast one upper case letter") 
   if not has_lower:
        print("add atleast one lower case letter")
   if not has_digit:
         print("add atleast one digit from 0-9")    
   if not has_special:
        print("add atleast one special character") 
        
elif score <=4: 
    print("Medium password")
    print("Suggestions:")
    if length<8:
       print("make the password of atleast 8 characters")
    if not has_upper: 
        print("add atleast one upper case letter") 
    if not has_lower:
        print("add atleast one lower case letter")
    if not has_digit:
         print("add atleast one digit from 0-9")     
    if not has_special:
        print("add atleast one special character") 

else:
    print("Strong Password") 
    
print(password)
print(has_upper)
print(has_lower)
print(has_digit)
print(has_special) 