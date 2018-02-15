from celery import Celery


app = Celery('tasks', broker='amqp://localhost//')  # or IP of remote

@app.task
def reverse(string):
    return string[::-1]
