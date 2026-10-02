################################################################ Password strength ############################################################


# password = input("Enter your password: ")
# length = len(password)
# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False
# score = 0
# for ch in password:
    
    
#         if ch.isupper() :
#            has_upper=True
           
#         elif ch.islower():
#            has_lower = True
#         elif ch.isdigit():
#            has_digit = True
#         else:
#            has_special = True
           
# if length>=8:
#     score +=1

# if has_upper:
#     score +=1
    
# if has_lower:
#     score +=1    

# if has_digit:
#     score +=1 
    
# if has_special:
#     score +=1   
    
# if score<=2:
#    print("Weak password")
#    print("Suggestions:")
#    if length<8:
#        print("make the password of atleast 8 characters")
#    if not has_upper:
#         print("add atleast one upper case letter") 
#    if not has_lower:
#         print("add atleast one lower case letter")
#    if not has_digit:
#          print("add atleast one digit from 0-9")    
#    if not has_special:
#         print("add atleast one special character") 
        
# elif score <=4: 
#     print("Medium password")
#     print("Suggestions:")
#     if length<8:
#        print("make the password of atleast 8 characters")
#     if not has_upper: 
#         print("add atleast one upper case letter") 
#     if not has_lower:
#         print("add atleast one lower case letter")
#     if not has_digit:
#          print("add atleast one digit from 0-9")     
#     if not has_special:
#         print("add atleast one special character") 

# else:
#     print("Strong Password") 
    
# print(password)
# print(has_upper)
# print(has_lower)
# print(has_digit)
# print(has_special)                                
                                 
            
            
            
############################################################### To-Do list ########################################################################   

# class Task:
#     def __init__(self,task,priority):
#         self.task = task
#         self.priority = priority
#         self.completed = False
        
#     def complete_task(self):
#         self.completed = True
    
#     def display(self):
#         status = "Completed" if self.completed else "Pending"
#         print(f"[{status}] {self.task} | Priority: {self.priority}")    
        
        
# class ToDoList:
#     def __init__(self):
#         self.tasks = []
                    
#     def add_task(self):
#         task = input("Enter task:")
#         priority = input("enter priority (High/Medium/Low):")
#         self.tasks.append(Task(task,priority))
        
#         with open("tasks.txt", "a") as f:
#             f.write(f"{task},{priority},Pending\n")
#         print("Task Added Successfully")                
        
        
#     def view_task(self):
#         if len(self.tasks)  ==0:
#             print("No Tasks Available")
            
#         else:
#             print("\nTasks:")
#             for i , task in enumerate(self.tasks,1):
#                 print(i, end=". ")
#                 task.display()           
                
#     def delete_task(self):
#         self.view_task()
        
#         if len(self.tasks) == 0:
#             return
#         index = int(input("Enter task number to delete: "))
#         self.tasks.pop(index-1)
#         with open("tasks.txt", "w") as f:
#             for task in self.tasks:
#                 status = "Completed" if task.complete else "Pending"
#                 f.write(f"{task},{task.priority},Pending\n")
        
        
#         print("Task Deleted Successfully")  
        
#     def complete_task(self):
#         self.view_task()
        
#         if len(self.tasks) == 0:
#             return
        
#         index = int(input("Enter Task number to complete:"))
#         self.tasks[index-1].complete_task()
        
#         with open("tasks.txt", "w") as f:
#             for task in self.tasks:
#                 status = "Completed" if task.complete else "Pending"
#                 f.write(f"{task},{task.priority},{status}\n")
                
#         print("Task marked as Completed!")              
        
        
# todo =  ToDoList()

# while True:
#     print("         TO-DO LIST         ")
#     print("1. Add Task")  
#     print("2. View Task")
#     print("3. Delete Task")
#     print("4. Complete Task")
#     print("5. Thankyouu ji")
    
#     try:
#         choice = int(input("Enter your choice:"))
        
#         if choice==1:
#          todo.add_task()
        
#         elif choice==2:
#          todo.view_task()
        
#         elif choice==3:
#          todo.delete_task()
         
#         elif choice==4:
#          todo.complete_task() 
         
        
        
#         elif choice==5:
#          print("Thankuuu jii")
#          break
    
#         else:
#          print("Invalid choice")
         
#     except ValueError:
#         print("Please enter numbers only")
        
#     except IndexError:
#         print("Invalid Task Number")
        
#     except Exception as e:
#         print("Error:" , e)        
        
             
    
    
        
        
    
        
   
