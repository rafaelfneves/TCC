# Imports
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Date, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models
from collector import Collector
from material import Material


