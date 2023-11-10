from __init__ import *
from models import db

class User(db.Model):
    __tablename__ = 'users'

    cpf_login = Column(String(11), primary_key=True)
    password_hash = Column(String, nullable=False)
    role = Column(Integer, nullable=False, checkconstraint="role IN (0, 1)")
