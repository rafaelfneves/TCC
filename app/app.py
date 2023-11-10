from __init__ import *

# ====================== [CONEXAO] ======================
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/collectors/listar"}})

db_config = {
    'dbname': 'greenline',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432',
}
migrate = Migrate(app, db)

# Initialize the db instance with the app
db.init_app(app)

app = Flask(__name__)
app.register_blueprint(collectors_bp, url_prefix='/collectors')
app.register_blueprint(materials_bp, url_prefix='/materialss')
app.register_blueprint(collectors_bp)

# Crie a URL de conexão com o PostgreSQL
db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# CHAVE SECRETA
app.config['SECRET_KEY'] = os.urandom(24)

# ====================== [MENU] ======================
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