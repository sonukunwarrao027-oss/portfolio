from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

#create database
def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS contact(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       email TEXT,
                       message TEXT
                       
                   )
                   """)
    conn.commit()
    conn.close()
    
create_database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO contact(name,email,message) VALUES(?,?,?)",
            (name,email,message)
        )
        conn.commit()
        conn.close()
    
  
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)