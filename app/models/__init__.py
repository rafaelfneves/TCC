# ====================== [INIT] ======================
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Date, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

