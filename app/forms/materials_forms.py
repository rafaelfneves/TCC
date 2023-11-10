from __init__ import *

class MaterialsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    fk_categories = IntegerField('Category ID', validators=[DataRequired()])
    
class MaterialsUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    fk_categories = IntegerField('Category ID', validators=[DataRequired()])