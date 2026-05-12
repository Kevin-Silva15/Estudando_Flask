from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


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
login_manager = LoginManager(app)
#aqui é ´ra redirecionar o usuario pra pagina de login, caso ele n esteja logado
login_manager.login_view = 'homepage'
bcrypt = Bcrypt(app)

# Rotas
from app.routes import homepage
from app.models import Contato

