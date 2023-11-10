from __init__ import *

class Address(db.Model):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, nullable=False)
    entity_type = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(String)
    complement = Column(String)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
