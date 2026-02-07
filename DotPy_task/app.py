import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

# Load the model (replace with your model's path)
model = YOLO("traffic_signs_model.pt")  # Path to your saved .pt file

st.title("Traffic Sign Detection with YOLOv8")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Convert to OpenCV format for inference
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Run inference
    results = model(img_cv)
    
    # Draw bounding boxes
    annotated_img = results[0].plot()  # Plots boxes on the image
    
    # Convert back to PIL for display
    annotated_pil = Image.fromarray(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
    
    # Display results
    st.image(annotated_pil, caption="Detected Traffic Signs", use_container_width=True)
    
    # Show detection details
    if len(results[0].boxes) > 0:
        st.write("Detected Signs:")
        for box in results[0].boxes:
            cls = int(box.cls)
            conf = float(box.conf)
            st.write(f"- {model.names[cls]} (Confidence: {conf:.2f})")
    else:
        st.write("No traffic signs detected.")