# Django Threads to Run Async Tasks

This is a quick demo to demonstrate how to use Ajax, Django, and threading to create asychronous tasks. When developing any Django app, or any other web
application, you should not make the browser wait for long running tasks which risk gateway timeouts and decreased UX. There is a lot of documentation
on using Django with Celery and/or Redis to perform asynchronous tasks, but it is likely overkill for most situations. A good native alternative uses
the Python threading package run tasks.

## Requirements

 - Python3
 - Django2.1


## Setup

```
git clone https://github.com/nbwoodward/django-async-threading.git
cd django-async-threading
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

In browser go to `http://localhost:8000`.
