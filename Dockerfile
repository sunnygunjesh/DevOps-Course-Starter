# Create Docker container from python image
FROM python:3.8.4-buster as Base

# Download  Poetry
RUN echo "Downloading Poetry"
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:/root/.poetry/bin"

# Create Workdir and copy the app
WORKDIR /DevOps-Course-Starter
COPY . /DevOps-Course-Starter
RUN poetry install

# Expose the port
EXPOSE 5000

# Create Dev environment from Base image
FROM base as development

RUN echo "Development environment"

# Install and run poetry
RUN echo "Running Poetry"
ENTRYPOINT ["poetry","run","flask","run","--port","5000","--host","0.0.0.0"]

# Create Prod environment from Base image
FROM base as production


RUN echo "Production environment"

# Setting Environment as Production
ENV FLASK_ENV=production

# Run Gunicorn 
RUN poetry add gunicorn
ENTRYPOINT ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000" ,"todo_app.app:app"]