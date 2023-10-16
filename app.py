from flask import Flask, request, jsonify, render_template, url_for
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
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
