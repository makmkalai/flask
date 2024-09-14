from flask import Flask,render_template,request,session,redirect,url_for
app=Flask(__name__)
app.secret_key="kalai"



@app.route("/",methods=["GET","POST"])
def login():
    user="kalai"
    password="kalai"
    if request.method=="POST":
        usn=request.form.get("username")
        pwd=request.form.get("password")
        if usn==user and pwd==password:
            session["username"]=usn
            return redirect(url_for("nav"))
        else:
            return "check it"
    return render_template("login.html")


@app.route("/navbar")
def nav():
    return render_template("index.html")

employee_details=[
        {"Name":"Mathav","Age":24,"Year_of_join":2020,"Salary":40000,"Place":"tensaki"},
        {"Name":"Kalyani","Age":24,"Year_of_join":2021,"Salary":30000,"Place":"tensaki"},
        {"Name":"Selva","Age":24,"Year_of_join":2022,"Salary":20000,"Place":"tensaki"},
        {"Name":"Hari","Age":24,"Year_of_join":2023,"Salary":10000,"Place":"tensaki"}
        ]

@app.route("/details")
def details():
    return render_template("data.html",emp1=employee_details)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        year_of_join=request.form.get("year_of_join")
        salary=request.form.get("salary")
        place=request.form.get("place")
        emp_dic={}
        emp_dic.update({"Name":name})
        emp_dic.update({"Age":age})
        emp_dic.update({"Year_of_join":year_of_join})
        emp_dic.update({"Salary":salary})
        emp_dic.update({"Place":place})
        employee_details.append(emp_dic)
        return redirect(url_for("details"))
    return render_template("add.html",emp=employee_details)


@app.route("/edit/<int:index>",methods=["GET","POST"])
def edit(index):
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        year_of_join=request.form.get("year_of_join")
        salary=request.form.get("salary")
        place=request.form.get("place")

        emp_list=employee_details[index-1]

        emp_list["Name"]=name
        emp_list["Age"]=age
        emp_list["Year_of_join"]=year_of_join
        emp_list["Salary"]=salary
        emp_list["Place"]=place
        return redirect(url_for("details"))
    epl=employee_details[index-1]
    return render_template("edit.html",emp1=epl)

@app.route("/delete/<int:index>")
def delete(index):
    employee_details.pop(index-1)
    return redirect(url_for("details"))

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True)