from flask import Flask,render_template, request
#import mysql.connector
import mariadb
import sys
from flask_sqlalchemy import SQLAlchemy
#from models import db, User

#def init_db():
 #   db.init_app(app)
  #  db.app = app

db = SQLAlchemy()

app = Flask(__name__)
#db.init_app(app)

#mydb = mysql.connector.connect(
try:
    conn = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='bat123',
         database='registered_users'
)
    print("coneected")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

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
        

    #user = User.query.filter_by(email=email).first() to search is user there
        #new_user = User(email=email, name=name, password=password)
    if username and email  and password:
        cur.execute("INSERT into user_register(email,username,password) values(%s,%s,%s)",(email,username,password,))
        conn.commit()
    return render_template('signup.html')
#conn.close()

if __name__ == "__main__":
    #app.init_db()
    app.run()