from FlaskApp import app
from flask import render_template, request

from VK import getPost
from .forms import IndexForm, MapLikesForms
from wordRate import wordRateFlask
from likeInCity import counterLike


@app.route('/')
def index_view():
    form = IndexForm()
    form_map = MapLikesForms()
    return render_template('index.html', form=form, form_map=form_map)


@app.route('/result', methods=['POST'])
def result_view():
    vk_id = request.form['vk_id']
    return render_template('result.html', dict=wordRateFlask(vk_id))


@app.route('/map_likes', methods=['POST'])
def map_likes_view():
    cities = counterLike(request.form['vk_id'], getPost([request.form['vk_id']])[0]['id'])
    return render_template('mapLikes.html', coord=cities)
