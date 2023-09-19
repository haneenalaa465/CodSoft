# Face Detection and Recognition

This project is designed for Face Detection and Recognition using Python and OpenCV. It allows you to upload an image or a video, detect faces in it, and perform face recognition if there are multiple faces detected.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Face Detection](#face-detection)
- [Face Recognition](#face-recognition)

## Prerequisites

Before using this project, make sure you have the following dependencies installed:

- Python (>=3.6)
- OpenCV
- matplotlib
- Google Colab (if you're using the Colab environment)
- deepface (for face recognition)

## Installation

You can install the required Python packages using pip:

```bash
pip install opencv-python-headless matplotlib deepface
```
## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/haneenalaa465/CodSoft.git
```
2. Navigate to the project directory:

```bash
cd CodSoft/Face-Detection-and-Recognition
```
3. Run the `Face_Detection_and_Recognition.ipynb` Jupyter Notebook using Jupyter or Google Colab.

## Face Detection
The project includes face detection capabilities, allowing you to upload an image or video and detect faces in it. It uses the Haar Cascade Classifier for face detection.

## Usage
- Upload an image or video file when prompted.
- The program will display the input with rectangles around detected faces and labeled with "face_X" where X is the face number.

## Face Recognition
If multiple faces are detected in the image, the project also includes face recognition capabilities using the DeepFace library. It compares the similarities between the detected faces.

## Usage
- Ensure that there are multiple faces detected in the image.
- The program will display the detected faces with labels and calculate the similarity score between each pair of faces.
