from flask import Flask
from flask_celery import make_celery


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'redis://'

celery = make_celery(app)

@app.route('/process/<name>')
def process(name):

    reverse.delay(name)

    return 'I sent an async request!'

@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]

if __name__ == '__main__':
    app.run(debug=True)
