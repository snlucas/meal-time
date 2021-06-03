# Set base image (host OS)
FROM python:3.8.6

# By default, listen on port 5000
# EXPOSE 5000/tcp

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN mkdir templates

COPY application.py .
COPY meal_functions.py .
COPY templates/ templates/

# Specify the command to run on container start
CMD [ "python", "./application.py" ]
