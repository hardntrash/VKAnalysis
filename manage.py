from FlaskApp import app

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'iuhiuh3iu1h2o3h1oui2h3981h23921u098123i12'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
