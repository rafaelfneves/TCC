from __init__ import *

class AddressForm(FlaskForm):
    street = StringField('Street', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])