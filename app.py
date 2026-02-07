import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "0"

import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

@st.cache_resource
def load_model():
    return YOLO("./Traffic_signs_model.pt")

model = load_model()

st.title("Traffic Sign Detection with YOLOv8")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    results = model(img_cv)

    annotated_img = results[0].plot()
    annotated_pil = Image.fromarray(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))

    st.image(annotated_pil, caption="Detected Traffic Signs", use_container_width=True)

    if results[0].boxes:
        for box in results[0].boxes:
            cls = int(box.cls)
            conf = float(box.conf)
            st.write(f"{model.names[cls]} — {conf:.2f}")
