from app import *
from forms import *

# ======== [MODELS] ========
from models.__init__ import Materials, db

# ======== [FORMS] ========
from forms.collectors_forms import CollectorForm, CollectorsUpdateForm
from forms.collectors_forms import CollectorForm, CollectorsUpdateForm

# ======== [Blueprints] ========

# -> Collectors
collectors_bp = Blueprint("collectors", __name__)
collectors_bp.template_folder = 'templates'

# -> Materials
materials_bp = Blueprint("materials", __name__)
materials_bp.template_folder = 'templates'