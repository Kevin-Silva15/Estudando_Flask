from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# comando pra criar o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# desabilitando a chegaquem a qualquer alteração
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# definindo nossa varialvel do banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Rotas
from app.routes import homepage
from app.models import Contato

