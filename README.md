# server-status-backend

Backend side of https://github.com/Daniil-Aleshechkin/server-status


## Installation ##

Requires any Linux or Mac OS system (Celery does not support windows)

- Install RabbitMQ https://www.rabbitmq.com/
- Install python https://www.python.org/

### Get the packages ###

>pip install -r serverManaager/requiremtents.txt

### Set up and run the project ###

>python .\manage.py makemigrations 
>python .\manage.py migrate
>python .\manage.py runserver

### Run the celery worker and scheduler ###

>celery -A serverManager worker --beat --scheduler django --loglevel=info

### Ensure that rabbitmq has started ###

Fedora

>sudo systemctl start rabbitmq-server
