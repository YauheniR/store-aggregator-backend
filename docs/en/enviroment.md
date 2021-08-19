# Environment variables

[Русский](../ru/enviroment.md) | **English**

Part of the project settings is taken from environment variables. 
To define them, create a **.env.example** file next to **manage.py** in the **src** folder and write the data there in this format: **VARIABLE=value**.

The following variables are available:

- **COMPOSE_PROJECT_DIR** - the directory where the project will be located inside the container;
- **COMPOSE_SH_DIR** - ${COMPOSE_PROJECT_DIR}/docker/backend
- **PROJECT_HOST** - allowed hosts that django can access;
- **POSTGRES_DB** - used to define a different name for the default database that is created when the image is first launched;
- **POSTGRES_PORT** - the port on which the database will run;
- **POSTGRES_HOST** - the host on which the database will run;
- **POSTGRES_USER** - used together with * * POSTGRES_PASSWORD** to set the user and his password;
- **POSTGRES_PASSWORD** - the environment variable sets the superuser password for PostgreSQL;
- **DEBUG** - debug mode. Set * * True** to see the debugging information in case of an error. It is disabled by the value * * False**.
- **SECRET_KEY** - the secret key for a specific Django installation.
This is used to provide a cryptographic signature and should have a unique unpredictable value;
- **ADMIN_USER_NAME** - login to log in to the admin panel;
- **ADMIN_USER_PASSWORD** - administrator password;
- **BROKER_HOST** - the host on which the broker works;
- **BROKER_PORT** - the port on which the broker works;
- **BROKER_VHOST** - vhost that will be accessed by celery via amqp;
- **BROKER_USER** - broker login;
- **BROKER_PASSWORD** - the broker's password;