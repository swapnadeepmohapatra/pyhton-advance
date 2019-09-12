import cv2
import time
import pandas
import datetime

firstFrame = None
statusList = [None, None]
times = []
df = pandas.DataFrame(columns=['Start', 'End'])
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = camera.read()
    status = 0
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.GaussianBlur(grayImage, (21, 21), 0)

    print(check)
    print(frame)

    if firstFrame is None:
        firstFrame = grayImage
        continue

    deltaFrame = cv2.absdiff(firstFrame, grayImage)
    threshFrame = cv2.threshold(deltaFrame, 30, 255, cv2.THRESH_BINARY)[1]
    threshFrame = cv2.dilate(threshFrame, None, iterations=0)
    (cnts, _) = cv2.findContours(threshFrame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    statusList.append(status)
    statusList = statusList[-2:]

    if statusList[-1] == 1 and statusList[-2] == 0:
        times.append(datetime.datetime.now())
    if statusList[-1] == 0 and statusList[-2] == 1:
        times.append(datetime.datetime.now())

    cv2.imshow('2', grayImage)
    cv2.imshow('3', deltaFrame)
    cv2.imshow('4', threshFrame)
    cv2.imshow('1', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# print(i)

for i in range(0, len(times), 2):
    df = df.append({'Start': times[i], 'End': times[i+1]}, ignore_index=True)

df.to_csv('Times.csv')

camera.release()
cv2.destroyAllWindows()
