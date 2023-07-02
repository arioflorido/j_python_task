# Use an official Python runtime as an image
FROM python:3.8

# The EXPOSE instruction indicates the ports on which a container
# will listen for connections
EXPOSE 8001

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /code

ENV DATABASE_URL='mysql+pymysql://root:root@db:3306/recipe_db'

# Install any needed packages specified in requirements.txt
COPY ./Pipfile ./Pipfile.lock /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv
RUN pipenv install --system

COPY . /code/

# Run app when the container launches
CMD ["python", "main.py"]
