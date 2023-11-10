from __init__ import *
from models import db

class Achievement(db.Model):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    requirement = Column(String)
    points = Column(Integer)
    fk_collector = Column(String(11), ForeignKey('collectors.cpf'))
    collector = relationship('Collector')
