from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
app = Celery()

@app.task
def add(x, y):
    return x + y
