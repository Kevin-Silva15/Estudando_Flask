# models que é o responsavel por se comunicar com o banco de dados!
from app import db
from datetime import datetime

# criando a classe que é responsavel por criar as tabelas
# toda classe de baco de dados deve herdar a classe q ta dentro do db


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