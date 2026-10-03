# Developmental Information
This page is for developmental information and communication between project partners. 

The application is built with Flask. You can visit the documentation here: [Flask_Documentation](https://flask.palletsprojects.com/en/stable/)

For the most part Flask development should be kept minimal.
All it needs it to pass a set data structure to the 
front end and we dont have to worry too much but as we progress
we will consider intergration and organse as needed.

Simply having it run in command line or direct queries is fine for now. We can easily abstract it out to Flask.

A note about the code below, i dont know if windows
need '\' or '/' so you can infer if it doesnt work.

Feel free to just push to main, if its a major break can roll back, but we shouldn't have 
too many issues with merging and such. But we'll handle as we go. 

Futhermore all logic should exist in [src/backend](src/backend/).
Frontend will just be for basic GUI and I/O [src/frontend](src/frontend/)

## Installing and Beginning
If you wish to install explicitly you will need to open a virtual enviroment to load dependancies for the application and Flask framework. 

You can install the required depenancies using:
```bash
# Bash
# Run to check if you ahve uv
uv --version

# Install in MacOS
brew install uv

# Clone the project, then go to folder
git clone <repository-url>
cd 3005_Project/application

# Run sync to build depenencies
uv sync
```

```powershell
# PowerShell
# Run to check if you ahve uv
uv --version

# Install UV on windows
winget install --id=astral-sh.uv -e

# Clone the project, the got to folder
git clone <repository-url>
cd 3005_Project\application

# Run
uv sync
```

## Running the applicaiton
The application runs a local server on [127.0.0.1](http://127.0.0.1:5000)

You can visit the link provided or visit in your browser: http://127.0.0.1:5000

To begin the application you can run the following:
```
uv run flask --app src/backend/app.py run
```

You can run in debug mode if you need.
This will automatically reload the server when code
changes occur.
```
flask --app hello run --debug
```

## Dependancies
If you need to add an import you can run the following:
```
uv add <package>
```
To remove one you no longer need
```
uv remove <package>
```
If you have an imported error when you pull from
git you can run the following to ensure packages are up to date.
```
uv sync
```

