# Visual Recognition System

This project comprises two visual recognition systems: **License Plate Recognition** and **Facial Recognition**, both developed using Python and various libraries.

## Introduction

The **Visual Recognition System** project demonstrates the implementation of two distinct recognition systems:

1. **License Plate Recognition**: Detects and recognizes text from license plates in images using OpenCV and Pytesseract.
2. **Facial Recognition**: Identifies and verifies human faces in images utilizing facial recognition libraries.

These systems showcase the application of computer vision techniques for real-world scenarios.

## Features

- **License Plate Recognition**:
  - Detects license plates in input images.
  - Extracts and recognizes text from detected license plates.

- **Facial Recognition**:
  - Detects human faces in input images.
  - Identifies and verifies recognized faces against a known dataset.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - OpenCV
  - Pytesseract
  - face_recognition
  - NumPy

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AkashDeore15/visual_recognition_system.git
   cd visual_recognition_system
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Additional Setup for License Plate Recognition**:
   - Install Tesseract-OCR on your system.
     - **Windows**: Download the installer from the [official repository](https://github.com/tesseract-ocr/tesseract) and follow the installation instructions.
     - **macOS**: Use Homebrew:
       ```bash
       brew install tesseract
       ```
     - **Linux**: Use the package manager:
       ```bash
       sudo apt-get install tesseract-ocr
       ```

   - Ensure the Tesseract executable is in your system's PATH.

## Usage

1. **License Plate Recognition**:
   - Place the input images containing license plates in the designated directory.
   - Run the script:
     ```bash
     python license_plate_recognition.py --image path_to_image
     ```
   - The script will display the detected license plate and recognized text.

2. **Facial Recognition**:
   - Prepare a dataset of known faces and ensure they are properly labeled.
   - Run the script:
     ```bash
     python facial_recognition.py --image path_to_image
     ```
   - The script will detect faces in the image and attempt to identify them based on the known dataset.

## Project Structure

- `license_plate_recognition.py`: Script for license plate detection and recognition.
- `facial_recognition.py`: Script for facial detection and recognition.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Make Your Changes and Commit Them**:
   ```bash
   git commit -m 'Add new feature'
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature-branch
   ```
5. **Open a Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
