# Server for IntroVerse project

This is the flask server for Queens of Code's project IntroVerse. IntroVerse is a website which started out as our final project for the CFGdegree. It is designed to be a safe nurturing environment for introverts who love anime, reading and gaming; to get recommendations, discuss and connect with others, and find resources, both for mental wellbeing and times of need.

## Prerequisites

This project uses MySQL for the development and testing databases. However, if you do not have MySQL it is also possible to run it with a SQLite database. To do this, open config.py and change the database connections in the DevConfig and TestConfig classes to use the sqlite DB variables instead. It hasn't been developed with SQLite in mind, so is not tested, but it should be possible.

## Set up

1. Create a virtual python environment (can do this with command or VScode should prompt you when try to run a file) and select it.

```
python -m venv venv
```

2. Install the required packages with pip (or pip3 for mac).

```
pip install -r requirements.txt
```

3. Set up the .env file, can create a copy of (or rename) .env.example and save as .env. Follow the instructions to add a secret key and your MySQL credentials.
4. Create the databases, either through the SQL script or with Python. Running create_db.py will create them if they don't exist or print if they do.

```
python create_db.py
```

5. Create tables of the development database through the SQL script or running create_tables.py (recommended). Can use flask migrate, flask db upgrade, to get the latest migrations of tables. Alternatively you can also uncomment with app context db.create_all in the app.py factory function.

```
python create_tables.py
```

```
flask db upgrade
```

6. Insert the book, game, and anime data from the SQL script file into your database so that can use the recommendation feature.
7. Run app.py to start the server

```
python app.py
```

Enjoy!

## How it is built and features

The frontend of our website uses React and the backend uses Flask. The backend also uses SQLAlchemy and MySQL as the database, and Flask-RESTX (a fork of Flask-RESTPlus) with the swagger docs for the server on the base path. Tests have been written using unittest, in the hope of covering the most common scenarios but welcome to suggestions.<br><br>
The API features are:

- User registration, login, and logout, which uses flask-jwt-extended (and react-auth-token on the frontend)
- Endpoints to view and edit profile
- Forum message board with ability to create, read, edit, and delete posts
- Filtering for forum messages based on category and author
- Content recommendation API for books, anime, and games (this is currently fairly limited in size for demonstration but we intend to grow it)
- Filtering for recommendations based on various fields such as author, console, genre etc

## Structure

The backend structure of this project is depicted below.

```
flask-server
├── migrations
├── models
|  ├── content_models.py
|  ├── forum_models.py
|  └── user_models.py
├── routes
|  ├── content.py
|  ├── forum.py
|  └── user.py
├── tests
|  ├── mock_data.py
|  ├── test_anime_api.py
|  ├── test_auth_api.py
|  ├── test_books_api.py
|  ├── test_forum_api.py
|  ├── test_games_api.py
|  └── test_user_api.py
├── venv
├── .env
├── .env.example
├── app.py
├── config.py
├── create_db.py
├── create_tables.py
├── exts.py
├── introverseSQL.sql
├── README.md
└── requirements.txt
```

- migrations - Folder containing the flask migrate files
- models - Contains the database model classes split according to namespace
- routes - Contains the different API namespaces and endpoints as well as their respective data transfer objects
- tests - Contains all the test files for each of the API endpoints and mock data file for content filtering tests, uses the testing database (also MySQL by default)
- venv - Virtual environment files
- .env and .env.example - Environment variables file (create and fill in if does not exist) and template
- app.py - Factory function for creating the app and run file
- config.py - Application config classes for connecting to database with the app
- create_db.py - Can run to create databases or check if they exist
- create_tables.py - Can run to create tables if want to
- exts.py - Extensions file, contains an instance of SQLAlchemy and JWTManager so that they can be imported into app.py and other files from one place
- introverseSQL.sql - SQL database file containing table creation if wish and the data to insert for recommendation API
- README.md - This guy
- requirements.txt - Requirements to pip install

## Troubleshooting and known issues

### Pip requirements

If you have any issues with modules not being installed properly try pip install manually. If you are a windows user you may have to do this instead:

```
pip install --user -r requirements.txt
```

If they are installed but the file shows things not imported properly try changing the Python interpreter (Ctrl+Shift+P in VS code) and then reinstalling packages if necessary. Have the virtual environment selected.

### Environment variables

The config.py file will use the environment variables from .env to connect to your database in MySQL. The load_dotenv function loads them so they can be used. However, if you have system environment variables of the same name it will use those unless override is set to true. "USER" is a common one, we found this out the hard way when database would not connect on another computer, so added override=True.

```
load_dotenv(override=True)
```

### Localhost 5000

This server uses the default port for Flask (5000) and the frontend is set up to use endpoints with that localhost. Mac users may need to disable AirPlay which also runs on port 5000 (we found this out the hard way as well from our Mac user).

## Useful docs

[Flask](https://flask.palletsprojects.com/en/3.0.x/)\
[SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)\
[Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/)\
[Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)\
[Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)\
[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
