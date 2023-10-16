from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib # para criar o codigo do voucher 
import re #para validar formato de e-mail


app = Flask(__name__)
# Configuração do banco de dados PostgreSQL (substitua com suas próprias configurações)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    #Retornará apenas a tarefa e a ideia dessa tarefa que acabou de ser criada.
    def __repr__(self):
        return '<Task %r>' % self.id

# ====================== [MAIN ROUTE] ======================
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        # Tentará criar uma nova tarefa a partir dessa entrada, e tentar-a enviá-la ao nosso banco de dados
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Houve um problema adicionando sua tarefa'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    
    except:
         return 'Houve um problema deletando sua tarefa'
     
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Houve um poblema atualizando sua tarefa'
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
