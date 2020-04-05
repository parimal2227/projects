from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class PredictionForm(FlaskForm):
    crim = StringField('CRIM', validators=[DataRequired()])
    zn = StringField('ZN', validators=[DataRequired()])
    indus = StringField('INDUS', validators=[DataRequired()])
    chas = StringField('CHAS', validators=[DataRequired()])
    nox = StringField('NOX', validators=[DataRequired()])
    rm = StringField('RM', validators=[DataRequired()])
    age = StringField('AGE', validators=[DataRequired()])
    dis = StringField('DIS', validators=[DataRequired()])
    rad = StringField('RAD', validators=[DataRequired()])
    tax = StringField('TAX', validators=[DataRequired()])
    pt_ratio = StringField('PTRATIO', validators=[DataRequired()])
    b = StringField('B', validators=[DataRequired()])
    l_stat = StringField('LSTAT', validators=[DataRequired()])
    submit = SubmitField('Prediict')

