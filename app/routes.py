from app import app, db
from flask import render_template, url_for, request, redirect
from app.models import Contato, Post
from app.forms import ContatoForm, UseForm, LoginForm, PostForm, PostComentariosForm
from flask_login import login_user, logout_user, current_user, login_required

#rota principal
@app.route('/',methods=['GET','POST'])
def homepage():
    usuario = 'Kevin'
    idade = 22
    form =LoginForm()

    # # trazer o usuario que esta logado
    # print(current_user)
    # #trazer a informação se tem alguem logado
    # print(current_user.is_authenticated)
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
    context = {
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html',context=context, form=form)

@app.route('/Cadastro', methods=['GET','POST'])
def cadastro():
    form = UseForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('Cadastro.html', form=form)

@app.route('/sair')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/post/novo', methods=['GET','POST'])
@login_required
def PostNovo():
    form = PostForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('homepage'))
    return render_template("PostNovo.html",form=form)
    
@app.route('/post/lista/')
@login_required
def PostLista():
    posts = Post.query.all()
    print(current_user.posts)

    return render_template("PostLista.html",posts=posts )

@app.route('/post/<int:id>/', methods=['GET','POST'])
@login_required
def PostDetail(id):
    post = Post.query.get(id)
    form = PostComentariosForm()
    if form.validate_on_submit():
        form.save(current_user.id, id)
        return redirect(url_for('PostDetail', id=id))

    return render_template('post.html',post=post,form=form)





@app.route('/contato', methods=['GET','POST'])
@login_required
def contato():
    form = ContatoForm()
    context={}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
        
    return render_template("contato.html",context=context, form=form)

@app.route('/contato/lista')
@login_required
def contato_lista():
    #aqui da pra fazer um if e deixar so adm apagar as coisa que nem queria lá no bd
    if current_user.id == 1:
        return redirect(url_for('homepage'))
    
    if request.method == "GET":
        pesquisa = request.args.get('pesquisa','')

    dados = Contato.query.order_by('nome')

    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
   
    context = {'dados':dados.all()}
    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>/')
@login_required
def contatoDetail(id):
    obj = Contato.query.get(id)

    return render_template('contato_detail.html', obj=obj)













#Formato não tão seguro
@app.route('/contato_old', methods=['GET','POST'])
@login_required
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



