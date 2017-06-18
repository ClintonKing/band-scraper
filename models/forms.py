from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class search_form(Form):
    search_field= StringField('search_field', validators=[DataRequired()], render_kw={"placeholder": "Enter band name"})

class search_again(Form):
    search_field = StringField('search_field', validators=[DataRequired()], render_kw={"placeholder": "Try another"})
