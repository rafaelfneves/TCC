# ====================== [MODELS] ======================
from __init__ import *

db = SQLAlchemy()

db_config = {
    'dbname': 'greenline',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432',
}

# Crie a URL de conexão com o PostgreSQL
db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}'

# ====================== [MODELS] ======================
from collector import Collector
from material import Material
