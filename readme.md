
# RTSP Object Detection

RTSP Object Detection is a project that combines real-time streaming protocol (RTSP) with object detection using the YOLOv5 model and Flask web framework. It provides a solution for detecting objects in a live video stream retrieved from an RTSP camera and rendering the results through a Flask endpoint.

## Features

- Simulates a surveillance camera by streaming a video as an RTSP stream on repeat.
- Performs real-time object detection on the RTSP stream using the YOLOv5 model.
- Provides a Flask endpoint to receive requests for object detection and returns the path of the output image with detected objects.
- A python script that sends a request to the inference container and prints the path of the output image.
- 
## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/AhmadWaly/RTSP_OBJECT_DETECTION.git
    cd RTSP_OBJECT_DETECTION
    ```
2. Make sure all the paths in the docker compose file are same path to the cloned repo
3. Start all containers:

    ```bash
    docker-compose up 
    ```
4. Send a request to the Flask endpoint for object detection:
open another terminal
    ```
    python3 ./client.py
    ```

## Directory Structure

```
RTSP_OBJECT_DETECTION/
│
├── inference/
│   ├── app.py
│   └── requirements.txt
│   └── Dockerfile
├── rtsp_camera/
│   ├── rtsp_server.yml
│   └── video.mp4
│
├── docker-compose.yml
├── client.py
├── restaurant-system-design.drawio
```

## Dependencies

- Docker
- Python 3.x
- OpenCV
- PyTorch
- Flask

