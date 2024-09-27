## Description
This web application is purely bulit to help prevent loneliness around teens and older also, connect them to people they can speak to, this website also offers resources on where to get help if you require it. We achieve this by creating a community where anyone can posts anything on there minds.

# Frontend
Follow the following steps to get frontend of application running in your terminal;
```
1. cd my-app
```
```
2. npm install
```
```
3. npm start
```
```
4. Enjoy exploring our website.
```

# Backend
See [Flask Readme](flask-server/README.md) for more information
## To set up and run the server
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
