# DevOps Apprenticeship: Project Exercise

 This project is to create a GUI for the Trello app using REST api. One can initiate the app and without login eplicitly to the Trello app on their website, can maintain work status. 

 This web-app uses flask, portry, python, html and Trello login to function.    
 trello_mod contains the python codes to create the URL to invoke Trello api.
 trello_item contains the class for Trello cards
 env file contains the different boards, list and other IDs.
   

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

Above can be run in batch by using the setup.sh script 
The script installs PyEnv, pip, poetry. Clone the web-app and copy the environment variables

## Running app via Docker

## Build Development Docker image and Run the To-Do App
`$ docker build --target development --tag todo-app:dev .`
`$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source="$(pwd)/todo_app",target=/DevOps-Course-Starter/todo_app todo-app:dev`

## Build Production Docker image and Run the To-Do App
$ docker build --target production --tag todo-app:prod .
$ docker run --env-file ./.env -p 5000:5000 todo-app:prod

## Where to check and stop the app from running
Check the running of app on http://127.0.0.1:5000/

To stop, one to stop the container from running
