#Use official python runtime as a parent image
FROM python:3.9-slim

#Set the working directory in the container
WORKDIR /usr/src/app

#Copy requirements.txt into the container at /usr/src/app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app.
COPY . .

# Make port 80 available to the world outside this container.
EXPOSE 80

# Define environment variable.
ENV NAME World

# Run app when the container launches.
CMD ["uvicorn", "model.api:app", "--host", "0.0.0.0", "--port", "80"]