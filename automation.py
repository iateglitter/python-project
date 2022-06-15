import cv2
import dropbox
import time
import random
starttime=time.time()
def takesnapshot():
    number = random.randint(0,100)
    cap = cv2.VideoCapture(0)
    result = True 
    while result:
        ret,frame = cap.read()
        image_name = "img"+str(number)+".png"
        starttime = time.time()
        cv2.imwrite("image1.jpg",frame)
        result = False
    cap.release()
    cv2.destroyAllWindows()

def uploadFile(imagename):
    accesstoken = "sl.BJjQpypQwEYRXJFb9Yn9LHurpmgBsY36d7MkaAW9EQFD4nBOk-FgMfYmGPEsEptJdftzxU8kDX5AqSNiIk6nAp81_OWBSIMbf4N_AVV1Ln-wPVsFVWTnppYNY19Q-89ZmxpHlC0"
    filefrom = imagename
    file2  = "/dropbox/"+imagename
    dbx = dropbox.Dropbox(accesstoken)
    with open(filefrom,"rb")as f:
        dbx.files_upload(f.read(), file2)

def main():
    while True:
        if time.time() - starttime >= 5:
            name = takesnapshot()
            uploadFile(name)

main()
