# models que é o responsavel por se comunicar com o banco de dados!
from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
# criando a classe que é responsavel por criar as tabelas
# toda classe de baco de dados deve herdar a classe q ta dentro do db

#para controle de login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    sobrenome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    senha = db.Column(db.String, nullable=True)
    posts = db.relationship('Post', backref='user', lazy=True)
    PostComentarios = db.relationship('PostComentarios', backref='user', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow())
    mensagem = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)
    PostComentarios = db.relationship('PostComentarios', backref='post', lazy=True)

    def msg_resumo(self):
        return f"{self.mensagem[:10]} ..."

class PostComentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_comentario = db.Column(db.DateTime, default=datetime.utcnow())
    comentario = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),nullable=True)




class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)

#Para todas as alterações feitas no arquivos models serão necessarias, rodar esses proximos comando
#1 fazer um commit
# flask db migrate -m "Nome qualquer"
# Com isso La no Version a gente achar esse commit

#2 rodar as alterações/ salvar o comitt nos bd
# flask db upgrade