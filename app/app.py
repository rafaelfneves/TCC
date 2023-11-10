# ====================== [APP.PY] ======================
from __init__ import CORS, db, db_url, Migrate, collectors_bp, materials_bp, Flask, render_template, os

# -> Initialize the Flask app
app = Flask(__name__, template_folder='views/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/collectors/select"}})
db.init_app(app)
migrate = Migrate(app, db)

# ======================= [BLUEPRINT] =======================
app.register_blueprint(collectors_bp, url_prefix='/collectors')
app.register_blueprint(materials_bp, url_prefix='/materials')
# ====================== [MENU] ======================
@app.route('/')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    with app.app_context():
        # Import your models here and create tables
        from models.collector import Collector
        db.create_all()
        print("Conexão com o PostgreSQL bem-sucedida.")

    app.run(debug=True)