import cv2 as cv
import numpy as np
import os

# loading haarcascade for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# load recognizer 
recognizer = cv.face.LBPHFaceRecognizer_create()

# loading face cam
cap = cv.VideoCapture(0)

# path of dataset 
dataset_path = 'training images'

face = []
labels = []

labels_to_name = {}
current_label = 0

# accessing the folders path in the dataset
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    
    if not os.path.isdir(person_folder) or not os.listdir(person_folder):
        continue
    
    # labeling the current folder name to person name
    labels_to_name[current_label] = person_name
   
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name) # accessing the image paths in the realated folder

        image = cv.imread(image_path, cv.IMREAD_GRAYSCALE) #  reading images and also converting them into grayscale

        face_rect = face_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 4) # detecting face in the dataset images

        for (x, y, w, h) in face_rect: # drawing a rectangle in faces of the dataset images 
            face_roi = image[x: x + w, y: y + h]

            if face_roi.size > 0:
                face_resize = cv.resize(face_roi, (200, 200))

                face.append(face_resize)
                labels.append(current_label)

    current_label += 1

if len(face) == 0:
    print('No Face found!')
    exit()


face = np.array(face)
labels = np.array(labels)

recognizer.train(face, labels) # training the model for face recognition
print('✅Training Complete!')

while True: # accessing the webcam 
    ret, frames = cap.read()
    grey = cv.cvtColor(frames, cv.COLOR_BGR2GRAY) # converting the frames into grayscale

    if not ret:
        break

    cam_face = face_cascade.detectMultiScale(grey, scaleFactor = 1.21, minNeighbors = 6) # detecting faces in the frames

    for (x, y, w, h) in cam_face: # drawing faces in the frames in realtime
        face_roi_grey = grey[y: y + h, x: x + w]
        
        if face_roi.size > 0:
            face_resize = cv.resize(face_roi_grey, (200, 200))

            label, f_confidence = recognizer.predict(face_resize) 
            actual_confidence = 100 - f_confidence   # calculating the actual confidence of the model in face recogmition

            if label in labels_to_name:
                person_name = labels_to_name[label]

                text = f'{person_name} - ({round(actual_confidence, 2)})'

                if actual_confidence >= 40:
                    print('Acces Granted!')
                    cv.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv.putText(frames, text, (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                else:
                    cv.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv.putText(frames, text, (x, y - 10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    cv.imshow('Face Recognition', frames)

    if cv.waitKey(1) & 0xFF == ord('k'):
        break


cap.release()
cv.destroyAllWindows() 


    








