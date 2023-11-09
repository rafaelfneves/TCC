from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from wtforms import StringField, DateField, DecimalField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf import FlaskForm
from models import Materiais, db

materiais_bp = Blueprint("materiais", __name__)
materiais_bp.template_folder = 'templates'

# ====================== [ROUTES] ======================
@materiais_bp.route('/')
def materiais():
    return render_template('menu_materiais.html')

# CADASTRAR
@materiais_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_materiais():
    form = MateriaisForm()  # Create an instance of the form

    if request.method == 'POST':
        data = request.json
        new_material = Materiais(**data)

        try:
            db.session.add(new_material)
            db.session.commit()
            return jsonify({'message': 'Material criado com sucesso'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return render_template('cadastrar_materiais.html', form=form)
    
# LISTAR
@materiais_bp.route('/listar', methods=['GET'])
def listar_materiais():
    materiais = Materiais.query.all()
    result = [{'id': material.id, 'nome': material.nome, 'categoria': material.categoria, 'valor_venda': material.valor_venda} for material in materiais]
    
    # Verificar se há um parâmetro 'deleted' na URL
    deleted = request.args.get('deleted')

    # Check the request format and respond accordingly
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        # If the request prefers JSON, return JSON
        return jsonify(result)
    else:
        # Otherwise, render the template
        return render_template('listar_materiais.html', materiais=materiais, deleted=deleted) 
    
@materiais_bp.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar_materiais(id):
    material = Materiais.query.get(id)
    form = MateriaisUpdateForm(obj=material)

    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(material)  # Atualize o objeto Material com os dados do formulário
        db.session.commit()
        flash('Material atualizado com sucesso', 'success')
        return redirect(url_for('materiais.listar_materiais'))

    return render_template('atualizar_materiais.html', material=material, form=form)

# DELETAR
@materiais_bp.route('/delete/<int:id>', methods=['DELETE','GET'])
def deletar_materiais(id):
    material = Materiais.query.get(id)

    if material:
        # Remova o Material do banco de dados
        db.session.delete(material)
        db.session.commit()
        # Redirecione de volta para a página de listagem com uma mensagem de confirmação
        return redirect(url_for('materiais.listar_materiais', deleted=True))
    else:
        # Se o Material não for encontrado, retorne uma mensagem de erro
        return jsonify({'error':'Material não encontrado'}), 404
    
# ====================== [FORMS] ======================
class MateriaisForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    descricao = TextAreaField('Descrição')
    categoria = StringField('Categoria', validators=[Length(max=50)])
    peso_medio_gramas = IntegerField('Peso Médio (g)', validators=[NumberRange(min=0)])
    valor_venda = DecimalField('Valor de Venda', validators=[NumberRange(min=0)], places=2)

class MateriaisUpdateForm(FlaskForm):
    id = HiddenField('ID')
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    descricao = TextAreaField('Descrição')
    categoria = StringField('Categoria', validators=[Length(max=50)])
    peso_medio_gramas = IntegerField('Peso Médio (g)', validators=[NumberRange(min=0)])
    valor_venda = DecimalField('Valor de Venda', validators=[NumberRange(min=0)], places=2)