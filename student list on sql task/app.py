from flask import Flask,render_template,request,url_for,session,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kalaidivi143'
app.config['MYSQL_DB'] = 'students_details'

app.secret_key="kalai"
mysql=MySQL(app)


@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        user=request.form.get("username")
        pwd=request.form.get("password")

        cur=mysql.connection.cursor()
        cur.execute("select * from stud where username=%s",(user,))
        data=cur.fetchone()
        cur.close()

        if data[1]==user and data[2]==pwd:
            session["username"]=user
            cur=mysql.connection.cursor()
            cur.execute("select * from stud where username=%s",(user,))
            onestd=cur.fetchone()
            cur.close()
            return render_template("index.html",std=onestd)
        else:
            return "invalid username and password"

    return render_template("login.html")
    
@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        user=request.form.get("username")
        pwd=request.form.get("password")

        cur=mysql.connection.cursor()
        cur.execute("select username from stud where username=%s",(user,))
        data=cur.fetchall()
        cur.close()
            
        if data==user:
            return "Username already exits"
        
        else:
            name=request.form.get("name")
            age=request.form.get("age")
            rollno=request.form.get("rollno")
            place=request.form.get("place")

            cur=mysql.connection.cursor()
            cur.execute("insert into stud(username,password,name,age,rollno,place) values(%s,%s,%s,%s,%s,%s)",(user,pwd,name,age,rollno,place))
            cur.connection.commit()
            cur.close()    

        return redirect(url_for('login')) 
        
    return render_template("signup.html")


# @app.route("/insert",methods=["GET","POST"])
# def insert():
#     if user and pwd:
#         name=request.form.get("name")
#         age=request.form.get("age")
#         rollno=request.form.get("rollno")
#         place=request.form.get("place")
#         cur=mysql.connection.cursor()
#         cur.execute("insert into stud(name,age,rollno,place) values(%s,%s,%s,%s)",(name,age,rollno,place))
#         cur.connection.commit()
#         cur.close()
#         return redirect(url_for('login'))
    # return render_template("index.html")

# @app.route("/home",methods=["GET","POST"])
# def home():
#     if request.method=="POST":
#         cur=mysql.connection.cursor()
#         cur.execute("select * from stud")
#         onestd=cur.fetchone()
#         cur.close()
#     return render_template("index.html",std=onestd)

    
        




if __name__=="__main__":
    app.run(debug=True)