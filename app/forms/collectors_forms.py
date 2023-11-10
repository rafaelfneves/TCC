from __init__ import *

class CollectorsForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    birth_date = DateField('Birth Date')
    phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired(), Email()])
    years_of_experience = IntegerField('Years of Experience')
    working_area = StringField('Working Area')
    

class CollectorsUpdateForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])    
    birth_date = DateField('Birth Date')
    phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired(), Email()])
    years_of_experience = IntegerField('Years of Experience')
    working_area = StringField('Working Area')