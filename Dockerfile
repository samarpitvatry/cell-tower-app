
# Use an official Python runtime as the parent image
FROM python:3.8.12-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8050 available to the world outside this container (Dash apps run on 8050 by default)
EXPOSE 8050

# Define environment variable for gunicorn to bind
ENV GUNICORN_CMD "gunicorn app:server --bind 0.0.0.0:8050"

# Run the command to start your app when the container launches
CMD ["sh", "-c", "$GUNICORN_CMD"]
