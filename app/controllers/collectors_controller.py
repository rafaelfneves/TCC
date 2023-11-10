from __init__ import *

# ====================== [ROUTES] ======================
@collectors_bp.route('/')
def collectors():
    return render_template('menu_collectors.html')


# CADASTRAR
@collectors_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_collectors():
    form = CatadorForm()  # Create an instance of the form

    if request.method == 'POST':
        data = request.json
        new_catador = Collectors(**data)

        try:
            db.session.add(new_catador)
            db.session.commit()
            return jsonify({'message': 'Catador criado com sucesso'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return render_template('register_collectors.html', form=form)
    
# SELECT
@collectors_bp.route('/listar', methods=['GET'])
def listar_collectors():
    collectors = Collectors.query.all()
    result = [{'id': collector.id, 'nome': collector.nome, 'sobrenome': collector.sobrenome} for collector in catadores]
    
    # Verificar se há um parâmetro 'deleted' na URL
    deleted = request.args.get('deleted')

    # Check the request format and respond accordingly
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        # If the request prefers JSON, return JSON
        return jsonify(result)
    else:
        # Otherwise, render the template
        return render_template('list_collectors.html', collectors=collectors, deleted=deleted)
    
@collectors_bp.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar_collectors(id):
    collector = Collectors.query.get(id)
    form = CollectorUpdateForm(obj=collector)

    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(collector)  # Atualize o objeto Catador com os dados do formulário
        db.session.commit()
        flash('Catador atualizado com sucesso', 'success')
        return redirect(url_for('catadores.listar_catadores'))

    return render_template('atualizar_catadores.html', catador=collector, form=form)

# DELETAR
@collectors_bp.route('/delete/<int:id>', methods=['DELETE','GET'])
def deletar_catadores(id):
    collector = Collectors.query.get(id)

    if collector:
        # Remova o catador do banco de dados
        db.session.delete(collector)
        db.session.commit()
        # Redirecione de volta para a página de listagem com uma mensagem de confirmação
        return redirect(url_for('catadores.listar_catadores', deleted=True))
    else:
        # Se o catador não for encontrado, retorne uma mensagem de erro
        return jsonify({'error':'Catador não encontrado'}), 404
    
