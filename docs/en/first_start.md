# First start

[Русский](../ru/first_start.md) | **English**

You can run the **store-aggregator-backend** project locally using **Pipenv**.

### Dependencies

* [pip3](https://github.com/pypa/pip)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Python 3.7.4](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

### Installation

First of all, installed [Pipenv](https://pypi.org/project/pipenv/),then run the commands:

     pip install pipenv
     
Go in the [backend](../..) folder and activate the environment:

    pipenv shell

Make sure that the environment has been created and activated.

Next, you need to install all the necessary packages for the application.

    pipenv install
    
The next step is to configure our local environment variables. 
You can read how to configure the environment variable file in the section [Environment variables](enviroment.md)

After everything has been configured, you can start the project. The first thing you need to do is perform migrations
to set up a database:

    python manage.py migrate

After all the above has been done, you can run project. To do this, run the command below,
it will allow you to run the project:

    python manage.py runserver

Now open the project in the [browser](http://localhost:8000).