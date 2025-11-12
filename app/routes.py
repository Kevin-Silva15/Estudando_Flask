from app import app
from flask import render_template, url_for;

#rota principal
@app.route('/')
def homepage():
    usuario = 'Kevin'
    idade = 22
    context = {
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html',context=context)

#rota principal
@app.route('/novo')
def novo():
    return 'novo'








