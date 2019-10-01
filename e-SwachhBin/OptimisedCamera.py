import cv2
import time

faceCascade = cv2.CascadeClassifier(
    'D:\\PythonAdvance\\OpenCV\\haarcascade_frontalface_default.xml')
faceCascade2 = cv2.CascadeClassifier(
    'D:\\PythonAdvance\\OpenCV\\haar_face.xml')

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# i = 1
while True:
    val = 'close'
    check, frame = camera.read()

    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(check)
    # print(frame)

    body = faceCascade.detectMultiScale(
        grayImage, scaleFactor=1.05, minNeighbors=6)

    faces = faceCascade2.detectMultiScale(
        grayImage, scaleFactor=1.05, minNeighbors=6)

    # print((faces))

    for x, y, w, h in faces:
        # frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        # frame = cv2.putText(frame, 'Face', (x, y - 10),
        #                     cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        if w > 220:
            val = 'open'

    # resized = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))
    # xAxis = int(frame.shape[1])
    # yAxis = int(frame.shape[0])
    # for x, y, w, h in body:
    #     frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #     frame = cv2.putText(frame, 'Body', (x, y - 10),
    #                         cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    # frame = cv2.putText(frame, val, (10, yAxis - 10),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10)

    # resized = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))

    # cv2.imshow('Capturing', resized)

    print(val)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
