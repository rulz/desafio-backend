import os
from fabric import task
import subprocess

@task
def run(c):
    os.environ.setdefault('DEBUG', 'True')
    subprocess.run(['python', 'manage.py', 'runserver', '0.0.0.0:8000'], check=True)

@task
def ma(c):
    os.environ.setdefault('DEBUG', 'True')
    subprocess.run(['python', 'manage.py', 'makemigrations'], check=True)

@task
def mi(c):
    os.environ.setdefault('DEBUG', 'True')
    subprocess.run(['python', 'manage.py', 'migrate'], check=True)

@task
def she(c):
    os.environ.setdefault('DEBUG', 'True')
    subprocess.run(['python', 'manage.py', 'shell_plus'], check=True)

@task
def createsuperuser(c):
    os.environ.setdefault('DEBUG', 'True')
    subprocess.run(['python', 'manage.py', 'createsuperuser'], check=True)
