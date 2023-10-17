from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib # para criar o codigo do voucher 
import re #para validar formato de e-mail

# ====================== [CONEXAO] ======================

app = Flask(__name__)

db_config = {
    'dbname': 'green_line',
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

# Teste a conexão
if db.engine.connect():
    print("Conexão bem-sucedida!")
else:
    print("Falha na conexão.")
    
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

# ====================== [ROTAS] ======================
# =-=-= [Rotas CRUD para Catadores] =-=-=
@app.route('/catadores', methods=['POST'])
def create_catador():
    data = request.json
    new_catador = Catadores(**data)
    db.session.add(new_catador)
    db.session.commit()
    return jsonify({'message': 'Catador criado com sucesso'}), 201

@app.route('/catadores', methods=['GET'])
def get_catadores():
    catadores = Catadores.query.all()
    result = [catador.__dict__ for catador in catadores]
    return jsonify(result)

@app.route('/catadores/<int:id>', methods=['GET'])
def get_catador(id):
    catador = Catadores.query.get(id)
    if catador:
        return jsonify(catador.__dict__)
    return jsonify({'message': 'Catador não encontrado'}), 404

@app.route('/catadores/<int:id>', methods=['PUT'])
def update_catador(id):
    data = request.json
    catador = Catadores.query.get(id)
    if catador:
        for key, value in data.items():
            setattr(catador, key, value)
        db.session.commit()
        return jsonify({'message': 'Catador atualizado com sucesso'})
    return jsonify({'message': 'Catador não encontrado'}), 404

@app.route('/catadores/<int:id>', methods=['DELETE'])
def delete_catador(id):
    catador = Catadores.query.get(id)
    if catador:
        db.session.delete(catador)
        db.session.commit()
        return jsonify({'message': 'Catador excluído com sucesso'})
    return jsonify({'message': 'Catador não encontrado'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)