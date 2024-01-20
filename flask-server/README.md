# Server for IntroVerse project
Description about IntroVerse Group 1 Project
## To set up and run the server
1. Create a virtual python environment (can do this with command or VScode should prompt you when try to run a file) and select it
```
python -m venv path
```
2. Install the required packages with pip
```
pip install -r requirements.txt
```
If you have any issues with modules not being installed properly try pip install manually. If you are a windows user you may have to do this instead:
```
pip install --user -r requirements.txt
```
If they are installed but the file shows not imported properly try changing the Python interpreter (Ctrl+Shift+P in VS code) and reinstalling if necessary. Have the virtual environment selected.
3. Set up .env file, can create a copy of (or rename) .env.example and save as .env, follow the instructions to add a secret key and MySQL credentials
4. Create the database if does not already exist - either through the SQL script or with Python
To create from Python run the create_db.py file
```
python create_db.py
```
5. Create the message_board table directly from the SQL file. Then the other tables (if do not already exist) can be created either through the SQL script or with Python (create_tables.py)
```
python create_tables.py
```
6. Insert the message_board, book, game, and anime data from the SQL file
7. Run routes.py to start the server
```
python routes.py
```
Enjoy!