from app import app, db
from flask import render_template, url_for, request, redirect
from app.models import Contato
from app.forms import ContatoForm

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


@app.route('/contato', methods=['GET','POST'])
def contato():
    form = ContatoForm()
    context={}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
        
    return render_template("contato.html",context=context, form=form)

@app.route('/contato/lista')
def contato_lista():

    if request.method == "GET":
        pesquisa = request.arg.get('pesquisa','')

    dados = Contato.query.order_by('nome')

    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
   
    
    contex = {'dados':dados.all()}

    return render_template('contato_lista.html', context=contex)





#Formato não tão seguro
@app.route('/contato_old', methods=['GET','POST'])
def contato_old():
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
        
    return render_template("contato_old.html",context=context)

#Usando o get, para resgatar o que o usuario solicitou
#apos fazer o formulario tendo o method = get, a gente faz um if na def da rota, para resgartar o get
#  if request.method == "GET": - Se a requisiç]ao foi get, ent faça:
#         pesquisa = request.arg.get('pesquisa') -jogue na variavel os argumento que veio do get chamado "pesquisa"(nome que for dado no input)
#         print(pesquisa) - Com isso eu resgatei o que foi solicitado pelo úsuario! 



