"""
This module (__init__.py) serves as the initialization file for the Flask application.
It includes necessary imports for libraries, blueprints, and other components.
"""

# ====================== [LIB] ======================
from flask import Flask, Blueprint, request, jsonify, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from wsgiref.validate import validator
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from flask_cors import CORS

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Date, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

from datetime import datetime

from wtforms import StringField, DateField, DecimalField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Optional, Length, NumberRange
# ======================= [MODELS] =======================
from models.models import db, db_url
# ====================== [OTHER LIB] ======================
import os # para gerar numeros aleatórios
import hashlib # para criar o codigo do voucher 
import re #para validar formato de e-mail
# ====================== [BLUEPRINT] ======================
# -> Collectors
collectors_bp = Blueprint('collectors', __name__, template_folder='templates/collectors')
collectors_bp.template_folder = 'templates'

# -> Materials
materials_bp = Blueprint('materials', __name__, template_folder='templates/materials')
materials_bp.template_folder = 'templates'