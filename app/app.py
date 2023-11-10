from . import *

# ====================== [CONEXAO] ======================

# CHAVE SECRETA
app.config['SECRET_KEY'] = os.urandom(24)

# MENU
@app.route('/')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    with app.app_context():
        # Import your models here and create tables
        from models import Collectors
        db.create_all()
        print("Conexão com o PostgreSQL bem-sucedida.")

    app.run(debug=True)