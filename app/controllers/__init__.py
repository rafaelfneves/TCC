from app import render_template, collectors_bp, materials_bp, request
from models.collector import Collector
from models.material import Material
from forms.__init__ import *
from models import db
from forms.collectors_forms import CollectorsForm, CollectorsUpdateForm
from forms.materials_forms import MaterialsForm, MaterialsUpdateForm