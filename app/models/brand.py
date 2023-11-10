from . import *

class Brand(db.Model):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
