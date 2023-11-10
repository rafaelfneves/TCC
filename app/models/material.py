from __init__ import *

class Material(db.Model):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    fk_categories = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')