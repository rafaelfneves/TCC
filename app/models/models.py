# ====================== [SQLALCHEMY] ======================
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

db_config = {
    'dbname': 'greenline',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432',
}

# Crie a URL de conexão com o PostgreSQL
db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}'
