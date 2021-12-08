# Use an official Python runtime as an image
FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container
# will listen for connections
EXPOSE 8001

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /code

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /code/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY . /code/

# Run app when the container launches
CMD ["python", "main.py"]
