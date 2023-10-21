# Xray-Fracture-Detection-YOLOv8

## Description

Welcome to the Xray-Fracture-Detection-YOLOv8 project, a robust fracture detection system based on the YOLOv8 model by Ultralytics. This model has been trained from scratch on a custom dataset of fractures in bone X-rays generously provided by the open-source community of Roboflow.

The repository contains a Flask web application (`app.py`) that runs locally on your machine. When executed, the web application prompts users to upload an X-ray image. Once an image is provided, the application processes it and highlights suspected fracture locations on the bone by drawing bounding boxes. Additionally, it displays the total number of fractures detected in the image.

## Getting Started

### Prerequisites

- Python 3.10.9
- Virtual environment (recommended)

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/Xray-Fracture-Detection-YOLOv8.git
   cd Xray-Fracture-Detection-YOLOv8
   ```

2. Create and activate a virtual environment (recommended but not mandatory):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies by running the following command in your virtual environment's terminal:

   ```shell
   pip install -r requirements.txt
   ```

### Running the Flask App

1. To start the Flask web application, run the following command in the terminal:

   ```shell
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000` to access the Xray Fracture Detection interface.

3. Upload an X-ray image for fracture detection, and the app will highlight suspected fracture locations.

## Acknowledgments

- YOLOv8 by Ultralytics
- Roboflow: [Website](https://roboflow.com)
