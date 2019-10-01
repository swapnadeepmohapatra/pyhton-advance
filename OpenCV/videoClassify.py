import cv2
import time

faceCascade = cv2.CascadeClassifier(
    'D:\\PythonAdvance\\OpenCV\\haar_face.xml')
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

i = 1
while True:
    i += 1
    check, frame = camera.read()

    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(check)
    print(frame)

    faces = faceCascade.detectMultiScale(
        grayImage, scaleFactor=1.05, minNeighbors=5)

    print((faces))

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        frame = cv2.putText(frame, 'id: ' + str(i), (x, y - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    resized = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))

    cv2.imshow('Capturing', resized)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(i)
camera.release()
cv2.destroyAllWindows()
