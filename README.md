## StockService
This project is a tool to generate some reports about some currency exchange data.
Basically, this is a Django project that uses django-restframework.

### Requirements

Python 3.8

## Quickstart:

* Activate your virtual environment

* install dependencies:

    ``make deps``

* Install pre-commit hooks:

    ``make setup``

* Start the database container:

    ``make startdb``

* Create the database (Only the first time):

    ``make createdb``

* Run the initials migrations:

    ``make migrate``

* Start the project

    ``make start``

* Stop the database

    ``make stopdb``

* Run test

    ``make test``

### Install
#### Create a virtual environment
Create a virtual environment and install required dependencies by executing:

`pip install -r requirements.txt` or using make `make deps`

#### Set up the project database
There are two options for this:

1. Using a PostgreSQL docker container (require install docker)
2. Using a local PostgreSQL database

To use a docker container, make sure you have installed docker before execute the
following command.

`docker exec -it dataservice_db createdb -U postgres stock_service`

or if you have make installed:

`make createdb` and after `make startdb` to start the database container.

To use a local PostgreSQL database, just configure a new database using '**stock_service**' as database
name using the postgres default port.

After that, execute database migrations:

`python manage.py migrate`

or if you have make installed:

`make migrate`

### Load currency data.
Now you have everything installed, you can populate your database by executing:

`python manage.py load_data <symbol>` for example `python manage.py load_data BTC-USD`

You can load as many symbols as you want, just make sure to do it one at a time.

Please **DO NOT LOAD THE SYMBOL DATA TWICE** since orders are unique. Due to this, try
to insert the same data into the database cause Duplicated key errors.
To update the data you need to reset the database:

`python manage.py reset_db`

or if you have make installed

`make reset_db`

After that, load the data again.

#### Check data
In case you want to check your loaded data, you can use de Django Admin.
Just create a superuser:

`python manage.py createsuperuser` or `make createsuperuser`

Run the application (see section _Run the application_) and then visit `localhost:8000/admin`,
login in using your username and password. Now you can check your data.

### Run the application.
Now that you have everything ready, run the application by executing:

`python manage.py runserver`

or using make:

`make start`

### Check json reports
To check available reports (three of them) over your data, just open a browser and visit
`http://localhost:8000/statistics/{symbol}/{report_type}`. For example:

`http://localhost:8000/statistics/BTC-USD/asks` to see Asks report
`http://localhost:8000/statistics/BTC-USD/bids` to see Bids report
`http://localhost:8000/statistics/BTC-USD/totals` to see total report

As a result you will a json like this (totals report example):

`{
    "data": {
        "BTC-USD": {
            "bids": {
                "count": 192,
                "qty": 92.81548968,
                "value": 1404201.1333760887
            },
            "asks": {
                "count": 243,
                "qty": 35.26452092,
                "value": 2644726.784921361
            }
        }
    }
}`

### Runnin test
To run the application tests just run:

`python manage.py test `

or using make:

`make tests`
