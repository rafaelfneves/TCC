# ====================== [LIB] ======================
from wsgiref.validate import validator
from flask import Flask, Blueprint, request, jsonify, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
from wtforms import StringField, DateField, DecimalField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Optional, Length, NumberRange
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf import FlaskForm

import os
import hashlib # para criar o codigo do voucher 
import re #para validar formato de e-mail

from models.__init__ import *
from controllers.__init__ import *

# ====================== [MODELS] ======================
from .models import db
from controllers.controllers import collectors_bp

# ====================== [BLUEPRINT] ======================
collectors_bp = Blueprint('collectors', __name__, template_folder='templates/collectors')
materials_bp = Blueprint('materials', __name__, template_folder='templates/materials')