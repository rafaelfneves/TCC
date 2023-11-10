from __init__ import *

# ====================== [MENU] ======================
@collectors_bp.route('/')
def menu_collectors():
    return render_template('collectors/menu_collectors.html')

# ====================== [CREATE] ======================
@collectors_bp.route('/create', methods=['GET', 'POST'])
def create_collectors():
    form = CollectorsForm()  # Create an instance of the form

    if request.method == 'POST':
        data = request.json
        new_collector = Collector(**data)

        try:
            db.session.add(new_collector)
            db.session.commit()
            return jsonify({'message': 'Catador criado com sucesso'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return render_template('collectors/create_collectors.html', form=form)
    
# ====================== [SELECT] ======================
@collectors_bp.route('/select', methods=['GET'])
def select_collectors():
    collectors = Collector.query.all()
    result = [{'cpf': collector.cpf, 'nome': collector.name, 'sobrenome': collector.surname} for collector in collectors]
    
    # Verificar se há um parâmetro 'deleted' na URL
    deleted = request.args.get('deleted')

    # Check the request format and respond accordingly
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        # If the request prefers JSON, return JSON
        return jsonify(result)
    else:
        # Otherwise, render the template
        return render_template('collectors/list_collectors.html', collectors=collectors, deleted=deleted)
    
# ====================== [UPDATE] ======================
@collectors_bp.route('/update/<string:cpf>', methods=['GET', 'POST'])
def update_collectors(cpf):
    collector = Collector.query.get(cpf)
    form = CollectorsUpdateForm(obj=collector)

    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(collector)  # Atualize o objeto Catador com os dados do formulário
        db.session.commit()
        flash('Catador atualizado com sucesso', 'success')
        return redirect(url_for('catadores.listar_catadores'))

    return render_template('collectors/atualizar_catadores.html', catador=collector, form=form)

# ====================== [DELETE] ======================
@collectors_bp.route('/delete/<string:cpf>', methods=['DELETE','GET'])
def deletar_collector(cpf):
    collector = Collector.query.get(cpf)

    if collector:
        # Remova o catador do banco de dados
        db.session.delete(collector)
        db.session.commit()
        # Redirecione de volta para a página de listagem com uma mensagem de confirmação
        return redirect(url_for('catadores.listar_catadores', deleted=True))
    else:
        # Se o catador não for encontrado, retorne uma mensagem de erro
        return jsonify({'error':'Catador não encontrado'}), 404
    
