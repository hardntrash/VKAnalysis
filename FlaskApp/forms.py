from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import Required

class FBIdForm(FlaskForm):
    fb_id = TextField(
    	'ID',
    	validators=[Required()],
    	render_kw={
    		"placeholder": "Введи id страницы",
    		"class": "input-line__input",
    	})
    submit = SubmitField(
    	'Go',
    	render_kw = {
    		"class": "input-line__submit",
    	})

class VKIdForm(FlaskForm):
    vk_id = TextField(
        'ID',
        validators=[Required()],
        render_kw={
            "placeholder": "Введи id пользователя",
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
