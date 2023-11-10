from __init__ import *

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
