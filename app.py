from wsgiref.validate import validator
from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired, Optional
from flask_cors import CORS
import hashlib # para criar o codigo do voucher 
import re #para validar formato de e-mail

# Modularização
from models import db
from catadores.routes import catadores_bp

# ====================== [CONEXAO] ======================
app = Flask(__name__)
app.register_blueprint(catadores_bp, url_prefix='/catadores')
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/catadores/listar"}})

db_config = {
    'dbname': 'greenline',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432',
}

# Crie a URL de conexão com o PostgreSQL
db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the db instance with the app
db.init_app(app)

# CHAVE SECRETA
app.config['SECRET_KEY'] = '123456'

# MENU
@app.route('/')
def menu():
    return render_template('menu.html')

# ========================= [DB] ==========================
if __name__ == '__main__':
    with app.app_context():
        # Import your models here and create tables
        from models import Catadores
        db.create_all()
        print("Conexão com o PostgreSQL bem-sucedida.")

    app.run(debug=True)