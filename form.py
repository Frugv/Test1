from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    InputA = IntegerField('a=', validators=[DataRequired()])
    InputB = IntegerField('b=', validators=[DataRequired()])
    InputC = IntegerField('c=', validators=[DataRequired()])
    submit = SubmitField('Далее')


