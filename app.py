from wsgiref.validate import validator
from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
from flask_wtf import FlaskForm
import jinja2
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired, Optional
import hashlib # para criar o codigo do voucher 
import re #para validar formato de e-mail

# ====================== [CONEXAO] ======================
app = Flask(__name__)

db_config = {
    'dbname': 'greenline',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432',
}

# Crie a URL de conexão com o PostgreSQL
db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}'

# Configure o SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

#CHAVE SECRETA
app.config['SECRET_KEY'] = '123456'

#Rota para a página inicial
@app.route('/')
def index():
    form = CatadorForm()  # Instancie o formulário aqui
    return render_template('index.html', form=form)  # Passe o formulário para o contexto do modelo
    
# ====================== [TABELAS] ======================
class Catadores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date)
    endereco = db.Column(db.String(255))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    experiencia_anos = db.Column(db.Integer)
    area_atuacao = db.Column(db.String(100))
    capacidade_carga_kg = db.Column(db.Numeric(10, 2))

class Conquistas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    requerimento = db.Column(db.String(255), nullable=False)
    pontos = db.Column(db.Integer, nullable=False)

class Empresas(db.Model):
    cnpj = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(255))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(20))

class Materiais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    categoria = db.Column(db.String(50))
    peso_medio_gramas = db.Column(db.Integer)
    valor_venda = db.Column(db.Numeric(10, 2))

class Veiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100))
    modelo = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    placa = db.Column(db.String(10))
    fk_catadores = db.Column(db.Integer, db.ForeignKey('catadores.id'))
    catador = db.relationship('Catadores', back_populates='veiculos')

class Vouchers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_conquistas = db.Column(db.Integer, db.ForeignKey('conquistas.id'))
    fk_empresas = db.Column(db.String(14), db.ForeignKey('empresas.cnpj'))
    fk_catadores = db.Column(db.Integer, db.ForeignKey('catadores.id'))
    codigo = db.Column(db.String(256), nullable=False)

#Forms
class CatadorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome')
    data_nascimento = DateField('Data de Nascimento')
    endereco = StringField('Endereço')
    cidade = StringField('Cidade')
    estado = StringField('Estado')
    telefone = StringField('Telefone')
    email = StringField('Email')
    experiencia_anos = DecimalField('Experiência em Anos', validators=[Optional()])
    area_atuacao = StringField('Área de Atuação')
    capacidade_carga_kg = DecimalField('Capacidade de Carga (kg)', validators=[Optional()])
    
# ====================== [ROTAS] ======================
# =-=-= [CRUD Catadores] =-=-=
@app.route('/catadores', methods=['POST'])
def create_catador():
    data = request.json
    new_catador = Catadores(**data)
    form = CatadorForm()
    try:
        db.session.add(new_catador)
        db.session.commit()
        return jsonify({'message': 'Catador criado com sucesso'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
#=====================================================
db_engine = create_engine(db_url)
try:
    db_engine.connect()
    print("Conexão com o PostgreSQL bem-sucedida.")
except Exception as e:
    print("Erro ao conectar ao PostgreSQL:", str(e))
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)




