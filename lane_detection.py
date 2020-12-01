import cv2
import numpy as np
import utils
import time
import serial

turn = []
avgVal=10
def getLaneCurve(img):
     
    # imgCopy = img.copy()
    # imgResult = img.copy()
    #### STEP 1
    imgThres = utils.thresholding(img)

    hT, wT, c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warpImg(imgThres,points,wT,hT)
    #imgWarpPoints = utils.drawPoints(imgCopy,points)
    mid,imgHist = utils.getHistogram(imgThres,display=True,minPer=0.5,region=4)
    base,imgHist = utils.getHistogram(imgThres,display=True,minPer=0.9)
    cur = base - mid
    turn.append(cur)
    if len(turn)>avgVal:
        turn.pop(0)

    curve = int(sum(turn)/len(turn))
    cv2.putText(img, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)
    imgStacked = utils.stackImages(0.7, ([img, imgHist, imgThres]))
    cv2.imshow('ImageStack', imgStacked)
  
    #cv2.imshow("warp", imgWarp)
    # cv2.imshow("thres", imgThres)
    # cv2.imshow("histogram", imgHist)
    return curve

 
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ser = serial.Serial('COM3', 115200, timeout=None)
    ser.flush()
    # initialT = [100,100,100,100]
    # utils.initializeTrackbars(initialT)
    while True:
        r, img = cap.read()
        img = cv2.resize(img,(480,240))
        curve = getLaneCurve(img)
        #print(curve)
        ser.write(b"%d\n" %(curve))
        #cv2.imshow('Vid',img)
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.075)
    cap.release()
    cv2.destroyAllWindows()
    
