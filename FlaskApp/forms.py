from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import Required

class IndexForm(FlaskForm):
    vk_id = TextField(
    	'ID',
    	validators=[Required()],
    	render_kw={
    		"placeholder": "Введи id",
    		"class": "input-line__input",
    	})
    submit = SubmitField(
    	'Go',
    	render_kw = {
    		"class": "input-line__submit",
    	})

class MapLikesForms(FlaskForm):
    vk_id = TextField(
       	'ID',
    	validators = [Required()],
    	render_kw = {
    		"placeholder": "Введи id группы или человека",
    		"class": "input-line__input",
    	})
    submit = SubmitField(
    	'Go Map',
    	render_kw = {
    		"class": "input-line__submit",
    	})