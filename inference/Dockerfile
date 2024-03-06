# Use an official Python runtime as a parent image
FROM python:3.9-slim


# # Copy the current directory contents into the container at /app
COPY . /inference

# Set the working directory in the container
WORKDIR /inference
# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]