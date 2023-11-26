# Setup

In order to run the project you will need Python 3.10 or greater and Django 4.2.7 or greater installed.

You will also need virtualenv installed. To do so, after installing python, type the following:

`pip install virtualenv`

After installing virtualenv it's time to create your env, inside ecomundo's folder type the following:

Linux:
`ecomundo$ python3 -m virtualenv .venv`
Windows:
`virtualenv .venv`

In order to activate the env type:

Linux:
`ecomundo$ source ./.venv/bin/activate`
Windows: 
`.venv/Scripts/Activate`

Now it's time to install the dependencies, this can be done typying the following command:

Linux: `ecomundo$ pip install requirements.txt`
Windows: pip install -r requirements.txt

To start project:
`python manage.py migrate`
`python manage.py runserver`
