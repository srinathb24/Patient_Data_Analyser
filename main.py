from flask import Flask,redirect,flash,url_for,render_template,request,session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)
app.secret_key="flask"

#config
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.permanent_session_lifetime = timedelta(minutes=5)

#model

db=SQLAlchemy(app)


def __init__(self,name,):
	self.name=name

#example	
dict1={"name":"srinath" ,"class":"12"}
dict2={"name":"bigboss" ,"class":"12"}
dict3={"name":"srinath" ,"class":"12"}
_list=[dict1,dict2,dict3]

@app.route("/table")
def table():
	return render_template("tabletemp.html",list=_list)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/login",methods=["POST","GET"])
def login():
	return


@app.route("/user",methods=["POST","GET"])
def user():
	return redirect(url_for("login"))

@app.route("/logout")
def logout():
	return redirect(url_for("login"))

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)
