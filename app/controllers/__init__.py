from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from wtforms import StringField, DateField, DecimalField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf import FlaskForm

from models import Materiais, db

from forms import collector

# Blueprints
collectors_bp = Blueprint("collectors", __name__)
collectors_bp.template_folder = 'templates'
