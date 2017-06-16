from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class url_form(Form):
    url_field = StringField('url_field', validators=[DataRequired()], render_kw={"placeholder": "Enter band name."})
