from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import Required

class IndexForm(FlaskForm):
    vk_id = TextField('ID', validators=[Required()])
    submit = SubmitField('Go')