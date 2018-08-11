from FlaskApp import app
from flask import render_template, request
from .forms import IndexForm
from wordRate import wordRateFlask

@app.route('/')
def index_view():
    form = IndexForm()
    return render_template('index.html', form=form)


@app.route('/result', methods=['POST'])
def result_view():
    vk_id = request.form['vk_id']
    return render_template('result.html', dict=wordRateFlask(vk_id))
