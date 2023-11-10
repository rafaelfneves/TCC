from . import *

class Collector(db.Model):
    __tablename__ = 'collectors'

    cpf = Column(String(11), primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date)
    phone = Column(String)
    email = Column(String, unique=True, nullable=False)
    years_of_experience = Column(Integer)
    working_area = Column(String)
