from __init__ import *
from models import db

class Company(db.Model):
    __tablename__ = 'companies'

    cnpj = Column(String(14), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
