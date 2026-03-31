import cv2 as cv
import numpy as np
import os # to navigate files/ folders 

# haarcascade load
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# load recognizer
recognizer = cv.face.LBPHFaceRecognizer_create()

dataset_path = 'training images'

faces = []
labels = []

labels_to_name = {}
current_label = 0

for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)

    if not os.listdir(person_folder):
        continue

    labels_to_name[current_label] = person_name

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

        if image is None:
            continue

        face_rect = face_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5)

        for (x, y, w, h) in face_rect:
            face_roi = image[y:y + h, x:x + w]
            face_resize = cv.resize(face_roi, (300, 300))

            faces.append(face_resize)
            labels.append(current_label)

    current_label += 1


faces = np.array(faces)
labels = np.array(labels)

recognizer.train(faces, labels)
print('✅ Training complete!')

test_img = cv.imread(r'pictures\IMG_20230916_154030_516.jpg')
test_resize = cv.resize(test_img, (700, 700))
test_grey = cv.cvtColor(test_resize, cv.COLOR_BGR2GRAY)

test_faces = face_cascade.detectMultiScale(test_grey, scaleFactor = 1.1, minNeighbors = 5)


for (x, y, w, h) in test_faces:
    face_roi = test_grey[y:y + h, x:x + w]
    face_resize = cv.resize(face_roi, (300, 300))

    label, confidence = recognizer.predict(face_resize)


    person_name = labels_to_name[label]

    cv.rectangle(test_resize, (x ,y), (x + w, y + h), (0, 255, 0), 2)
    text = f'{person_name}  ({round(confidence, 2)})'
    cv.putText(test_resize, text, (x , y - 10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,180), 2)


cv.imshow('Recognition Result', test_resize)
cv.waitKey(0)
cv.destroyAllWindows()






