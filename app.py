from flask import Flask,render_template, request,redirect
#import mysql.connector
import mariadb

#import pymysql

import sys
from flask_sqlalchemy import SQLAlchemy
from flask import flash
#from models import db, User

#def init_db():
 #   db.init_app(app)
  #  db.app = app

db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
db.init_app(app)

#mydb = mysql.connector.connect(
try:
    conn = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='bat123',
         database='registered_users')
#)
    print("coneected")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

#conn = pymysql.connect(host='127.0.0.1', port= 3306,  user='root',database='registered_users', passwd='bat123',  cursorclass=pymysql.cursors.DictCursor)
# Get Cursor
cur = conn.cursor()

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
      # user = User( username=request.form.get("username"),email=request.form.get("email"),password=request.form.get("password") )
    
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        #    print(row)rue
        #    print(row)
            #if(username==row):
            #    flash('User name already is taken.Please enter another one')
            #    user_exists=True

        if username and email  and password:
            try:
                cur.execute("INSERT into register_theuser(email,username,password) values(%s,%s,%s)",(email,username,password,))
                conn.commit()
                flash("Successfully registered","success")
                return render_template('index.html')
            except:
                flash("Username or email already exists.Please try again","danger")
                return render_template('signup.html')

    #user = User.query.filter_by(email=email).first() to search is user there
        #new_user = User(email=email, name=name, password=password)
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email_exists=0
        email = request.form.get('email')
        password = request.form.get('password')

        email_db=cur.execute("SELECT email FROM register_theuser")
        email_db=cur.fetchall()
        for row in email_db:
            for item in row:
               # print (str(item) ) 
                if(item==email):
                    email_exists=1
            
        if(email_exists==1):
            flash("Successfully logged in","success")
            return render_template('index.html')
        else:
            flash("Incorrect username or password","danger")
            flash("Please check your login details and try again.","danger")
            return render_template('login.html')
   
    return render_template('login.html')
#conn.close()

if __name__ == "__main__":
    #app.init_db()
    app.run()