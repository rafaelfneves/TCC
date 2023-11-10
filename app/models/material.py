from .__init__ import Flask, CORS, create_engine, ForeignKey, Column, String, Integer, CHAR, Date, Float, Text, relationship
from .models import db

class Material(db.Model):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    fk_categories = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
