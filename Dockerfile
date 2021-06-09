# Set base image (host OS)
FROM python:3.8.6

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set WorkDir
WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create dirs.
RUN mkdir templates
RUN mkdir static
RUN mkdir app

# Copy files
COPY application.py .
COPY templates/ templates/
COPY static/ static/
COPY app/ app/

# Specify the command to run on container start
CMD [ "python", "./application.py" ]
