# BLOG PROJECT
## project setup
First create a virtual envorement:
>$python -m venv blog_env

Then, activate:
>source blog_env/bin/activate

Then install the dependencies:
>(blog_env)$  pip3 install django

>(blog_env)$  pip3 install django-bootstrap-v5

>(blog_env)$ pip install -r requirements.txt

Once pip has finished downloading the dependencies:
>(blog_env)$  cd blog_project

>(blog_env)$ python manage.py runserver

And navigate to `http://127.0.0.1:8000/blog/`.
