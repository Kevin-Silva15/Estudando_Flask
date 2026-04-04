from app import app
from flask import render_template, url_for, request

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
@app.route('/contato')
def contato():
    context={}
    if request.method == "GET":
        pesquisa = request.args.get('pesquisa')
        print(pesquisa)
        context.update({'pesquisa':pesquisa})
    return render_template("contato.html",context=context)


#Usando o get, para resgatar o que o usuario solicitou
#apos fazer o formulario tendo o method = get, a gente faz um if na def da rota, para resgartar o get
#  if request.method == "GET": - Se a requisiç]ao foi get, ent faça:
#         pesquisa = request.arg.get('pesquisa') -jogue na variavel os argumento que veio do get chamado "pesquisa"(nome que for dado no input)
#         print(pesquisa) - Com isso eu resgatei o que foi solicitado pelo úsuario! 



