# First start

[Русский](../ru/first_start.md) | **English**

You can run the **store-aggregator-backend** project locally using **Pipenv**.

### Dependencies

* [Python 3.7.4](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker-Compose](https://docs.docker.com/composer/install/)

### Installation

First of all, install [Docker](https://docs.docker.com/engine/install/) and [Docker-Compose](https://docs.docker.com/composer/install/)

The next step is to configure the environment variables.
You can read how to configure the environment variables file in the [Environment Variables](enviroment.md)

After everything has been configured, you can run the project locally or deploy it in docker containers.

To run the project locally in [root](../..) for the project, run the command:

    make run_local

Now open the project in [browser](http://localhost:8000).

To run all project services in docker containers in [root](../..) for the project, run the command:

    make run_docker