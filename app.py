import pandas as pd
import csv
from flask import Flask, render_template, Response, request, redirect, url_for,flash
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def stud():
    return render_template("search-student.html")

@app.route("/add", methods=["GET"])
def get_form():
    return render_template("add-student.html")


@app.route("/sdet", methods=["POST"])
def post_form():
    sid = request.form.get("id")
    name = request.form.get("name")
    gender = request.form.get("gender")
    date = request.form.get("date")
    city = request.form.get("city")
    state = request.form.get("state")
    email= request.form.get("email")
    qualification = request.form.get("qualification")
    stream = request.form.get("stream")

    if sid == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if name == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if gender == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if date == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if city == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if state == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if email == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if qualification == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    if stream == "":
        return render_template("error.html", message="Please ensure all fields are filled out correctly")
    
    with open('students.csv', 'a', newline='') as f:
        writer1 = csv.writer(f)
        writer1.writerow([sid,name,gender,date,city,state,email,qualification,stream])
    print("Student added successfully")
    return render_template("index.html")

@app.route("/disp")
def display():
  
# to read csv file named "samplee" 
    a = pd.read_csv("students.csv") 
  
# to save as html file 
# named as "Table" 
    a.to_html("templates/Table.html") 
  
    return render_template("Table.html")

@app.route("/sr",methods=['POST'])
def search():
    b=[]
    n=str(request.form['student'])
    from csv import reader
    with open("students.csv", "r") as f:
        read1 = reader(f)
        for row in read1:
            if n in row:
                b=row

    return render_template('display-search.html',sid=b[0], 
                                         sname=b[1], 
                                         gender=b[2],
                                         dob=b[3],
                                         city=b[4],
                                         state=b[5],
                                         email=b[6],
                                         qual=b[7],
                                         stream=b[8])
if __name__=='__main__':
    import webbrowser
    webbrowser.open('http://localhost:5000')
    app.run()




