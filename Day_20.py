import cv2 as cv

cap = cv.VideoCapture(0)

faces_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    tr , frame = cap.read()
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faces_cascade.detectMultiScale(grey, scaleFactor = 1.1, minNeighbors = 5) # this return in tuples ((x, y, w, h))

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

    cv.imshow('Face_detectation', frame)

    if cv.waitKey(1) & 0xFF == ord('k'):
        break

cap.release()
cv.destroyAllWindows()