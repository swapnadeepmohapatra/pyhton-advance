import cv2

faceCascade = cv2.CascadeClassifier(
    'D:\\PythonAdvance\\OpenCV\\haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# img = cv2.imread('A:\\Assests\\431.jpg', 1)
check, frame = camera.read()
gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray_img, scaleFactor=1.05, minNeighbors=5)

print((faces))

i = 1
for x, y, w, h in faces:
    frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    frame = cv2.putText(frame, 'id: ' + str(i), (x, y - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    i += 1
resized = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))

cv2.imshow("grey", resized)
cv2.waitKey()
cv2.destroyAllWindows()
