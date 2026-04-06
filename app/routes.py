from app import app, db
from flask import render_template, url_for, request
from app.models import Contato

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
@app.route('/contato', methods=['GET','POST'])
def contato():
    context={}
    if request.method == "GET":
        pesquisa = request.args.get('pesquisa')
        print('GET:',pesquisa)
        context.update({'pesquisa':pesquisa})

    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )
        db.session.add(contato)
        db.session.commit()
        
    return render_template("contato.html",context=context)

#Usando o get, para resgatar o que o usuario solicitou
#apos fazer o formulario tendo o method = get, a gente faz um if na def da rota, para resgartar o get
#  if request.method == "GET": - Se a requisiç]ao foi get, ent faça:
#         pesquisa = request.arg.get('pesquisa') -jogue na variavel os argumento que veio do get chamado "pesquisa"(nome que for dado no input)
#         print(pesquisa) - Com isso eu resgatei o que foi solicitado pelo úsuario! 



