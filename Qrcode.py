import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
used_code=[]

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)

    for obj in decodedObjects:

        if obj.data.decode('utf-8') not in used_code:
            print( obj.data.decode('utf-8'))
            used_code.append(obj.data.decode('utf-8'))
            time.sleep(3)
        elif obj.data.decode('utf-8') in used_code:
            print("Sorry' this code has been used!!")
            time.sleep(3)
        else:
            pass

        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)


    cv2.imshow("Frame", frame)
    key=cv2.waitKey(1)
    if key==27:
        break


