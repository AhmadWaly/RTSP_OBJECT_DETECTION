# Use an official Python runtime as a parent image
FROM ultralytics/yolov5:latest-cpu

# Set the working directory in the container
WORKDIR /app

# # Copy the current directory contents into the container at /app
COPY ./inference .

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
