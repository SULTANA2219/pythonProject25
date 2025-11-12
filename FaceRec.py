#FaceRecognition App

import cv2
import face_recognition
import numpy as np
import os

#Path to folder with known faces (add images like 'person1.jpg', 'person2.jpg', 'person3.jpg')
KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6 #Lower values are stricted for matches
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn' #'cnn' for GPU, 'hog' for CPU

#Load known faces
known_faces = []
known_names = []

for name in
os.listdir(KNOWN_FACES_DIR):
  for filename in
  os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
    image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
    encoding = face_recognition.face_encodings(image) [0]
    known_faces.append(encoding)
    known_names.append(name)

#Initialize webcam
video = cv2.VideoCapture(0)

print('Loading...')

while True:
  ret, image = video.read()
  if not ret:
    break

locations = face_recognition.face_locations(image, model=MODEL)
encodings = face_recognition.face_encodings(image, locations)

for face_encoding, face_location in zip(encodings, locations):
  results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
  match = None
  if True in results:
    match = 
    known_names[results.index(True)]
    print(f'Match found: {match}')

top_left = (face_location[3], face_location[0])
bottom_right = (face_location[1], face_location[2])

color = [0, 255, 0] if 
    
