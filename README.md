# Traffic Sign Detection with YOLOv8 and Streamlit

## 📌 Project Overview

This project is a **Traffic Sign Detection web application** built using **YOLOv8 (Ultralytics)** for object detection and **Streamlit** for the user interface. The application allows users to upload an image and automatically:

* Detect traffic signs in the image
* Draw bounding boxes around detected signs
* Classify each detected sign into one of **four categories**:

  * **Prohibitory**
  * **Danger**
  * **Mandatory**
  * **Other**
* Display the **confidence (accuracy)** for each detected sign

The model used is a **pretrained YOLOv8n (nano) model**, fine-tuned specifically for traffic sign detection.

---

## 🎯 Main Objective

The main goal of this project is to perform an **object detection task** that:

1. Identifies traffic signs in an image
2. Classifies them into predefined categories
3. Provides confidence scores for each prediction
4. Presents results in a simple, interactive web interface

This can be useful for:

* Intelligent Transportation Systems (ITS)
* Autonomous driving research
* Traffic monitoring and safety analysis
* Educational and demonstration purposes

---

## 🧠 Model Details

* **Model Architecture:** YOLOv8n (Nano version)
* **Framework:** Ultralytics YOLO
* **Task Type:** Object Detection
* **Number of Classes:** 4

  * Prohibitory
  * Danger
  * Mandatory
  * Other
* **Model File:** `traffic_signs_model.pt`

YOLOv8n is lightweight and fast, making it suitable for real-time and web-based applications.

---

## 🖥️ Application Workflow

1. User uploads an image (`.jpg`, `.jpeg`, or `.png`)
2. The image is displayed in the Streamlit app
3. The image is converted to OpenCV format for inference
4. YOLOv8 runs object detection on the image
5. Bounding boxes and class labels are drawn
6. The annotated image is displayed
7. Detected classes and confidence scores are listed

---

## 📂 Project Structure

```
├── app.py                     # Main Streamlit application
├── traffic_signs_model.pt     # Trained YOLOv8 model
├── README.md                  # Project documentation
```

---

## ⚙️ Requirements

Make sure you have the following installed:

* Python 3.8+
* Streamlit
* Ultralytics
* OpenCV
* Pillow
* NumPy

You can install dependencies using:

```bash
pip install streamlit ultralytics opencv-python pillow numpy
```

---

## ▶️ How to Run the Application

1. Activate your virtual or Conda environment
2. Navigate to the project directory
3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Upload an image containing traffic signs
5. View detection results and confidence scores

---

## ✅ Key Benefits

* 🚀 Fast and efficient detection using YOLOv8n
* 🖼️ User-friendly web interface
* 📊 Displays confidence (accuracy) for each detected sign
* 🔧 Easy to extend with more classes or live video input
* 💡 Suitable for real-world traffic analysis scenarios

---

## 🔮 Future Improvements

* Add real-time webcam detection
* Support video file uploads
* Display confidence scores directly on bounding boxes
* Improve model accuracy with more training data
* Deploy the app using Docker or cloud services

---

## 📜 License

This project is intended for educational.

---

## 👤 Author

Developed by *[zeyad Elawady]*

If you have questions or want to extend this project, feel free to contribute or ask!
