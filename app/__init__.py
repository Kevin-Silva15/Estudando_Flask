from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv('.env')


app = Flask(__name__)
# comando pra criar o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# desabilitando a chegaquem a qualquer alteração
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Token de segurança
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# definindo nossa varialvel do banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Rotas
from app.routes import homepage
from app.models import Contato

