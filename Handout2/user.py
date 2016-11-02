# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	age = db.Column(db.Integer)
	height = db.Column(db.Integer)
	sex = db.Column(db.String(30))
	def __init__(self, username, email,age,height,sex):
    	   self.username = username
    	   self.email = email
    	   self.age = age
    	   self.height = height
    	   self.sex = sex

@app.route('/create', methods=['GET', 'POST'])
def add_user():
   if request.method == 'POST':
    	username = request.form["username"]
    	email = request.form["email"]
    	age = request.form["age"]
    	height = request.form["height"]
    	sex = request.form["sex"]
    	user = User(username=username, email=email, age=age, height=height, sex=sex)
    	db.session.add(user)
    	db.session.commit()
    	return " dado inserido"
   return '''
    	<form action="" method="post">
        	<p>usuário: <input type=text name=username>
        	<p>email: <input type=email name=email>
        	<p>idade: <input type=number name=age>
        	<p>altura: <input type=number name=height>
        	<p>sexo: <input type=text name=sex>
        	<p><input type=submit value=Inserir>
    	</form>
	'''
@app.route('/read/<username>')
def read_user(username):
	user = User.query.filter_by(username=username).first()
	if(user):
    	  return " username: &lt;" + user.username  + "&gt;"+ " e-mail: &lt;" + user.email + "&gt;"+ " age: &lt;" + str(user.age) + "&gt;"+ " height: &lt;" + str(user.height) + "&gt;"+ " sex: &lt;" + user.sex + "&gt;"   
    	  #&lt; Less than: <
		  #&gt; Greater than: > 
	else:
    	  return "Usuário não encontrado",404
@app.route('/update/<username>', methods=['GET', 'POST'])
def update_user(username):
   if request.method == 'POST':
    	username = request.form["username"]
    	email = request.form["email"]
    	age = request.form["age"]
    	height = request.form["height"]
    	sex = request.form["sex"]
    	user = User.query.filter_by(username=username).first()
    	user.email = email
    	user.age=age
    	user.height=height
    	user.sex=sex
    	db.session.commit()
    	return "Bem vindo"
   user = User.query.filter_by(username=username).first()
   return '''
    	<form action="" method="post">
        	<p>usuário: <input type=text name=username value={0}>
        	<p>email: <input type=email name=email value={1}>
        	<p>age: <input type=number name=age value={2}>
        	<p>height: <input type=number name=height value={3}>
        	<p>sex: <input type=text name=sex value={4}>
       	 <p><input type=submit value=Update>
    	</form>
	'''.format(username,user.email,user.age,user.height,user.sex)

@app.route('/delete/<username>')
def delete_user(username):
	user = User.query.filter_by(username=username).first()
	db.session.delete(user)
	db.session.commit()
	return "usuário removido"
@app.route('/list')
def list_user():
	users = User.query.all()
	return render_template('list.html',users=users)
db.create_all()
 
if __name__ == "__main__":
	app.run(host="0.0.0.0")