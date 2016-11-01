# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
app = Flask(__name__)

@app.route("/")
def root():
    return "<strong>Ola Mundo!</strong>"

@app.route("/about")
def about():
    return "Programa desenvolvido por: <em> Felipe Buniac </em>"

@app.route("/user/<name>")
def user(name):
	if name=="Felipe":
		return "Esta é a página de Felipe Buniac"
	else:
		return "Usuário {0} não encontrado".format(name)

@app.route('/people/')
@app.route('/people/<nick>')
def hello(nick=None):
    return render_template('people.html', name=nick)

@app.route("/product")
def product():
	productId = request.args.get('productId')
	if productId=='1':
		return "Produto: carro" 
	elif productId=='2': 
		return "Produto: casa"
	else:
		return "Produto não encontrado"
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != '1234':
        	return "Usuário não encontrado ou senha incorreta"
        else:
        	return "Bem vindo admin"
    return '''
        <form action="" method="post">
            <p>usuário: <input type=text name=username>
            <p>senha: <input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''
    return redirect("/static/login.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0")