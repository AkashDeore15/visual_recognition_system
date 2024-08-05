import cv2
import numpy as np
import pytesseract

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 200)
    return edges

def find_contours(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    return contours

def detect_license_plate(image):
    edges = preprocess_image(image)
    contours = find_contours(edges)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            plate = image[y:y + h, x:x + w]
            return plate
    return None

def recognize_text(plate_image):
    config = '--oem 3 --psm 7'
    text = pytesseract.image_to_string(plate_image, config=config)
    return text.strip()

if __name__ == "__main__":
    image_path = "path_to_license_plate_image.jpg"
    image = cv2.imread(image_path)
    plate_image = detect_license_plate(image)
    if plate_image is not None:
        plate_text = recognize_text(plate_image)
        print("License Plate Text:", plate_text)
    else:
        print("License plate not detected.")
