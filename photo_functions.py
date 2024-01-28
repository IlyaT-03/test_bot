import cv2
import cv2.data
import numpy as np


def contains_face(img_stream):
    image = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )
    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
    return len(face) > 0

