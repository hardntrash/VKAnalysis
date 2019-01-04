from FlaskApp import app
from flask import render_template, request

from VK import getPost
from .forms import FBIdForm, VKIdForm, MapLikesForms
from wordRate import wordRateVK, wordRateFB
from likeInCity import counterLike


@app.route('/')
def index_view():
    form_vk = VKIdForm()
    form_fb = FBIdForm()
    form_map = MapLikesForms()
    return render_template('index.html', form_vk=form_vk, form_fb=form_fb, form_map=form_map)

@app.route('/vk_result', methods=['POST'])
def vk_result_view():
    vk_id = request.form['vk_id']
    return render_template('result.html', dict=wordRateVK(vk_id))

@app.route('/fb_result', methods=['POST'])
def fb_result_view():
    fb_id = request.form['fb_id']
    return render_template('result.html', dict=wordRateFB(fb_id))

@app.route('/map_likes', methods=['POST'])
def map_likes_view():
    cities = counterLike(request.form['vk_id'], getPost([request.form['vk_id']])[0]['id'])
    return render_template('mapLikes.html', coord=cities)

