import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime

def recognize():    
    path='/home/parthasarathy/Downloads/face_recognition/images'
    images=[]
    classNames=[]
    myList=os.listdir(path)
    print(myList)

    #Adding images and classNames from directory(myList)
    for i in myList:
        curImg = cv2.imread(f'{path}/{i}')
        images.append(curImg)
        classNames.append(os.path.splitext(i)[0])
    print(classNames)

    #ENCODING
    def findEncodings(listOfImgs):
        encodeList=[]
        for img in listOfImgs:
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode=face_recognition.face_encodings(img)[0]
            encodeList.append(encode) 
        return encodeList
        
    # Marking the attendance
    def markAttendance(rno):
        with open('Attendance.csv','r+') as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split(',')
                if(len(entry)>1):
                    nameList.append(entry[1])
            
            if rno not in nameList:
                now = datetime.now()
                dtString=now.strftime('%d/%m/%Y')
                tString=now.strftime('%H:%M:%S')
                with  open ('Database.csv','r+') as d:
                    nameString=None
                    depString=None
                    secString=None
                    for row in d:
                        r=row.split(',')
                        if(len(r)>1):
                            temp=r[0]
                            if(temp==rno):
                                nameString=r[1]
                                depString=r[2]
                                yrString=[3]
                                secString=r[4]
                                print('found')
                                break
                f.writelines(f'\n{nameString},{rno},{dtString},{tString},{depString},{yrString},{secString}')  
                print(nameList)  

    encodeListKnown=findEncodings(images)
    print('Encoding Completed')

    def takeAttendance():
        global rno
        cap=cv2.VideoCapture(0)
        while True:
            success,img=cap.read()
            imgs=cv2.resize(img,(0,0),None,0.25,0.25)
            imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
            
            # Encoding the images from webcam
            facesCurFrame=face_recognition.face_locations(imgs)
            encodeCurFrame=face_recognition.face_encodings(imgs,facesCurFrame)    
            
            for encodeCurFace,faceLoc in zip(encodeCurFrame,facesCurFrame):
                matches=face_recognition.compare_faces(encodeListKnown,encodeCurFace)
                faceDis=face_recognition.face_distance(encodeListKnown,encodeCurFace)
                print(faceDis)
                
                # finding the best match with the lowest distance
                matchIndex=np.argmin(faceDis)
                if matches[matchIndex]:
                    name=classNames[matchIndex] #.upper()
                    rno=classNames[matchIndex]
                    name=name.split('_')[1]
                    rno=rno.split('_')[0]
                    print(rno)
                    
                    # Showing the rectangle and the name
                    y1,x2,y2,x1=faceLoc
                    y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),5)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    markAttendance(rno)
                    
            # Showing the webcam        
            cv2.imshow('Webcam',img)
            key=cv2.waitKey(1)
            if(key==27 or key==13):
                cap.release()
                cv2.destroyAllWindows()
    takeAttendance()

