import time

startTime=time.time()


def snapshot():
    import cv2
    cam = cv2.VideoCapture(0)

    result=True
    while result:
        startTime=time.time()
        ret, frame = cam.read()
        cv2.imwrite("test.jpg", frame)

        result=False


    cam.release()
    cv2.destroyAllWindows()

while(True):
    if(time.time()-startTime>100000):

        snapshot()


