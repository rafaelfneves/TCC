from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from wtforms import StringField, DateField, DecimalField
from wtforms.validators import DataRequired, Optional
from flask_wtf import FlaskForm
from models import Catadores, db

catadores_bp = Blueprint("catadores", __name__)
catadores_bp.template_folder = 'templates'

# ====================== [ROUTES] ======================
@catadores_bp.route('/')
def catadores():
    return render_template('menu_catadores.html')

# CADASTRAR
@catadores_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_catadores():
    form = CatadorForm()  # Create an instance of the form

    if request.method == 'POST':
        data = request.json
        new_catador = Catadores(**data)

        try:
            db.session.add(new_catador)
            db.session.commit()
            return jsonify({'message': 'Catador criado com sucesso'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return render_template('cadastrar_catadores.html', form=form)
    
# LISTAR
@catadores_bp.route('/listar', methods=['GET'])
def listar_catadores():
    catadores = Catadores.query.all()
    result = [{'id': catador.id, 'nome': catador.nome, 'sobrenome': catador.sobrenome} for catador in catadores]
    
    # Verificar se há um parâmetro 'deleted' na URL
    deleted = request.args.get('deleted')

    # Check the request format and respond accordingly
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        # If the request prefers JSON, return JSON
        return jsonify(result)
    else:
        # Otherwise, render the template
        return render_template('listar_catadores.html', catadores=catadores, deleted=deleted)
    

@catadores_bp.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar_catador(id):
    # Lógica para atualizar um catador pelo ID
    return f"Atualizar o catador com ID {id}"

# DELETAR
@catadores_bp.route('/listar/delete/<int:id>', methods=['DELETE','GET'])
def deletar_catador(id):
    catador = Catadores.query.get(id)

    if catador:
        # Remova o catador do banco de dados
        db.session.delete(catador)
        db.session.commit()
        # Redirecione de volta para a página de listagem com uma mensagem de confirmação
        return redirect(url_for('catadores.listar_catadores', deleted=True))
    else:
        # Se o catador não for encontrado, retorne uma mensagem de erro
        return jsonify({'error':'Catador não encontrado'}), 404
    
# ====================== [FORMS] ======================
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
   