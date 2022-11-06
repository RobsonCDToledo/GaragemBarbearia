from app import app
from flask import Flask,  render_template

@app.route('/')
@app.route('/index')

def index():
    nome = 'Luciano'
    dados = {'profissao': 'Barbeiro','endereco': 'Avenida Pedro Luiz da Costa, 155/1 - Costa Rios', 'cidade': 'Pouso Alegre-MG'}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
 