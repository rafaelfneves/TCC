from wsgiref.validate import validator
from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired, Optional
from flask_cors import CORS
from flask_migrate import Migrate

import os
import hashlib # para criar o codigo do voucher 
import re #para validar formato de e-mail

# Modularização
from .models import db
from controllers.controllers import collectors_bp


# Criação do Blueprint
from flask import Blueprint
collectors_bp = Blueprint('collectors', __name__)

# Importar as rotas após a criação do Blueprint
from . import routes

# ========================= [DB] ==========================

#app.register_blueprint(collectors_bp, url_prefix='/collectors')
#app.register_blueprint(materials_bp, url_prefix='/materialss')
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/collectors/listar"}})

db_config = {
    'dbname': 'greenline',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432',
}
migrate = Migrate(app, db)

# Initialize the db instance with the app
db.init_app(app)


app = Flask(__name__)
app.register_blueprint(collectors_bp)

# Crie a URL de conexão com o PostgreSQL
db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False