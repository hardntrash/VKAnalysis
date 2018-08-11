from FlaskApp import app

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'fuck-u'


if __name__ == '__main__':
    app.run(debug=True)