# Use the official Python 3.11 image from the Docker Hub
FROM python:3.11-slim

# Install aha package
RUN apt-get update && apt-get install -y aha && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

COPY Elyzer/* Elyzer/
COPY app/requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r Elyzer/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app/ .

# Command to run the application
CMD ["python", "main.py"]