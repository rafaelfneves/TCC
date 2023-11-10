from . import *

class Inventory(db.Model):
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True)
    material_name = Column(String, nullable=False)
    weight_grams = Column(Float, nullable=False)
    fk_materials = Column(Integer, ForeignKey('materials.id'))
    material = relationship('Material')
