import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

def load_facenet_model():
    model = load_model('facenet_keras.h5')
    return model

def preprocess_image(image, target_size=(160, 160)):
    image = cv2.resize(image, target_size)
    image = image.astype('float32')
    mean, std = image.mean(), image.std()
    image = (image - mean) / std
    return np.expand_dims(image, axis=0)

def get_embedding(model, image):
    preprocessed_image = preprocess_image(image)
    embedding = model.predict(preprocessed_image)
    return embedding

def recognize_faces(image, known_faces, known_labels, model):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        embedding = get_embedding(model, face)
        label = identify_face(embedding, known_faces, known_labels)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    
    return image

def identify_face(embedding, known_faces, known_labels):
    min_dist = float('inf')
    label = 'Unknown'
    
    for known_face, known_label in zip(known_faces, known_labels):
        dist = np.linalg.norm(embedding - known_face)
        if dist < min_dist:
            min_dist = dist
            label = known_label
    
    return label

if __name__ == "__main__":
    image_path = "path_to_facial_image.jpg"
    known_faces_path = "path_to_known_faces.npy"
    known_labels_path = "path_to_known_labels.npy"
    
    image = cv2.imread(image_path)
    known_faces = np.load(known_faces_path)
    known_labels = np.load(known_labels_path)
    
    model = load_facenet_model()
    recognized_image = recognize_faces(image, known_faces, known_labels, model)
    
    cv2.imshow('Facial Recognition', recognized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()