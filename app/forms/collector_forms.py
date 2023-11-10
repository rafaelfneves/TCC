from . import *

class CollectorForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    birth_date = DateField('Birth Date')
    phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired(), Email()])
    years_of_experience = IntegerField('Years of Experience')
    working_area = StringField('Working Area')
    

class UpdateCollectorForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    birth_date = DateField('Birth Date')
    phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired(), Email()])
    years_of_experience = IntegerField('Years of Experience')
    working_area = StringField('Working Area')