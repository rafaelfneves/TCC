from __init__ import *

class materialsController:
    @staticmethod
    def get_all_materials():
        materials = Material.query.all()
        return jsonify([material.serialize() for material in materials])

# ====================== [MENU] ======================
@materials_bp.route('/')
def materials():
    return render_template('menu_materials.html')

# ====================== [CREATE] ======================
@materials_bp.route('/create', methods=['GET', 'POST'])
def create_materials():
    form = MaterialsForm()  # Create an instance of the form

    if request.method == 'POST':
        data = request.json
        new_material = Material(**data)

        try:
            db.session.add(new_material)
            db.session.commit()
            return jsonify({'message': 'Material criado com sucesso'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return render_template('create_materials.html', form=form)
    
# ====================== [SELECT] ======================
@materials_bp.route('/select', methods=['GET'])
def select_materials():
    materials = Material.query.all()
    result = [{'id': material.id, 'nome': material.nome, 'categoria': material.categoria, 'valor_venda': material.valor_venda} for material in materials]
    
    # Verificar se há um parâmetro 'deleted' na URL
    deleted = request.args.get('deleted')

    # Check the request format and respond accordingly
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        # If the request prefers JSON, return JSON
        return jsonify(result)
    else:
        # Otherwise, render the template
        return render_template('select_materials.html', materials=materials, deleted=deleted) 
   
# ====================== [UPDATE] ====================== 
@materials_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_materials(id):
    material = Materials.query.get(id)
    form = MaterialsUpdateForm(obj=material)

    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(material)  # Atualize o objeto Material com os dados do formulário
        db.session.commit()
        flash('Material atualizado com sucesso', 'success')
        return redirect(url_for('materials.select_material'))

    return render_template('update_materials.html', material=material, form=form)

# ====================== [DELETE] ======================
@materials_bp.route('/delete/<int:id>', methods=['DELETE','GET'])
def deletar_materials(id):
    material = Material.query.get(id)

    if material:
        # Remova o Material do banco de dados
        db.session.delete(material)
        db.session.commit()
        # Redirecione de volta para a página de listagem com uma mensagem de confirmação
        return redirect(url_for('material.select_materials', deleted=True))
    else:
        # Se o Material não for encontrado, retorne uma mensagem de erro
        return jsonify({'error':'Material não encontrado'}), 404
    