from datetime import datetime

import cv2
import pyzbar.pyzbar as pyzbar

#cap variable stores live video from primary camera
cap = cv2.VideoCapture(r'D:\Prog\OpenCV\Python Project\Sample Video.mp4')

#font to print the data on the frame
font = cv2.FONT_HERSHEY_PLAIN

lastmsg="Rs 20 Toll Collected From : "
lastuser=""
while True:
    suc, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)

    #current time
    now = datetime.now()

    for obj in decodedObjects:
        
        #decoded data
        qrdata = str(obj.data)
        qrdata = qrdata[2:-1]
        #print(qrdata)

        #read  user data
        f = open("D:\\Prog\\OpenCV\\Python Project\\USER_DATA\\" + qrdata + ".txt", "r")

        userdata = f.read().splitlines()
        f.close()

        FMT = "%d/%m/%Y %H:%M:%S"
        #current time
        currtime = now.strftime(FMT)

        #date time format
        

        #calcualte time differnce
        tdelta = datetime.strptime(currtime, FMT) - datetime.strptime(userdata[1], FMT)

        #collecting toll
        if (tdelta.seconds > 300):
            lastuser=qrdata
            userdata[0] = str(int(userdata[0])-20 )

            f = open("D:\\Prog\\OpenCV\\Python Project\\USER_DATA\\" + qrdata + ".txt", "w")
            updateddata = userdata[0]+"\n"+currtime
            f.write(updateddata)

            f.close()
            #closed
            #i ran the code twice, it shows accepted, run the code, DSA

    cv2.putText(frame, lastmsg+lastuser, (20,450), font, 2,(255, 255, 255), 3)

    cv2.imshow("Toll", frame)

    #27=ESC KEY
    key = cv2.waitKey(1)
    if key == 27:
        break
