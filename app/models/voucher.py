from __init__ import *
from models import db

class Voucher(db.Model):
    __tablename__ = 'vouchers'

    cod_voucher = Column(Integer, primary_key=True)
    fk_achievements = Column(Integer, ForeignKey('achievements.id'))
    fk_companies = Column(String(14), ForeignKey('companies.cnpj'))
