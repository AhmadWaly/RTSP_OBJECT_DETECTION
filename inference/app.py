import argparse
import io
import os
from PIL import Image
import cv2
import torch
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def predict():
    
    stream = cv2.VideoCapture('rtsp://127.0.0.1:8554/stream')  # Replace with your actual RTSP URL
    
    ret, frame = stream.read()
    results = model([frame])

    results.render()  # updates results.imgs with boxes and labels
    results.save(save_dir="output_imgs/")
    n += 1
    return f"output_imgs/image{n}.jpg"



if __name__ == "__main__":
    n=0
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # force_reload = recache latest code
    model.eval()
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat