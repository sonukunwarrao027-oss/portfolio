# from flask import Flask

# app=Flask(__name__) 

# @app.route('/')
# def home():
#     return "Home Page"



# @app.route('/about')
# def about():
#     return "About Page"

# @app.route('/contact')
# def contact():
#     return "Contact Page"

# @app.route('/details')
# def details():
#     return "Details Page"



#static
# 

# @app.route('/user/gargi')
# def gargi():
#     return "gargi Page"

# @app.route('/user/chintu')
# def chintu():
#     return "chintu Page"

# @app.route('/user/monu')
# def monu():
#     return "monu Page"
#Dynamic page
# @app.route('/user/<name>')
# def user(name):
#     return f"Welcome {name}"

# app.run(debug = True)

# @app.route('/user/<int:marks>')
# def user(marks):
#     return f"Your marks {marks}"

# app.run(debug = True)



################################################################# Jinja2###############################################

#combine krna h flask k code ko python k code se

# from flask import Flask, render_template
# app=Flask(__name__)

# @app.route('/')
# def home():
#     students = ["Chintu","Sonu","PIPPO"]
#     # return render_template("home.html",name="Rahul",age = 25)
#     return render_template("home.html",students = students)
# app.run(debug=True)


####################################### API ########################

# from flask import Flask, render_template, request

# app=Flask(__name__)

# @app.route('/',methods = ['GET','POST'])
# def home():
    
#     if request.method =='POST':
        
#         username = request.form['username']
#         if username=="":
#             return"Username Required"
        
#         password = request.form['password']
#         if len(password)<8:
#             return "password is very short"
        
#         email=request.form['email']
        
        
#         return f"Hello {username}"
    
        
    
#     return render_template("form.html")

# app.run(debug=True)

import sqlite3 ## library of database
conn = sqlite3.connect("students.db") ##file hogi to access kr lega baki khud create kr lega

cursor=conn.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS students(
#                    id INTEGER PRIMARY KEY,
#                    name TEXT,
#                    age INTEGER
                    
                   
#                )
#                """)
# cursor.execute(
#     "INSERT into students (id,name,age) VALUES(?,?,?)",
#     (7,"Sonu",21)
# )   

# cursor.execute(
#     "INSERT into students (id,name,age) VALUES(?,?,?)",
#     (8,"Sonu",21)
# )   
# cursor.execute( 
#     "INSERT into students (id,name,age) VALUES(?,?,?)",
#     (9,"BHAWANIGOD",22)
# )
# cursor.execute(    
#     "INSERT into students (id,name,age) VALUES(?,?,?)",
#     (10,"Muskaan",21)
    
# )
# conn.commit()

# cursor.execute("select * FROM students")

# rows = cursor.fetchall()
# for row in rows:
#     print(row)
    
# conn.commit()
# conn.close()    

# from flask import Flask, render_template
# import sqlite3

# app = Flask(__name__)

# def get_db_connection():
    
#     conn = sqlite3.connect("students.db")
    
#     conn.row_factory = sqlite3.Row ##tuple ki jagah dict form m data aaajayga
    
#     return conn

# @app.route("/")
# def home():
    
#     conn = get_db_connection()
    
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT * FROM students")
    
#     students = cursor.fetchall()
    
#     conn.close()
    
#     return render_template("students.html",students=students)

# app.run(debug=True)



                           