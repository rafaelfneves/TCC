
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    veiculos = db.relationship('Veiculos', back_populates='catador')

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



