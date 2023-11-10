# ====================== [APP.PY] ======================
from __init__ import *

# -> Initialize the Flask app
app = Flask(__name__)
# ====================== [CONECTION] ======================

cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/collectors/select"}})

# Initialize the db instance with the app
db.init_app(app)

migrate = Migrate(app, db)

# Registra a Blueprint com o aplicativo
app.register_blueprint(collectors_bp, url_prefix='/collectors')
app.register_blueprint(materials_bp, url_prefix='/materials')
app.register_blueprint(collectors_bp)

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