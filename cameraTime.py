import cv2
import dropbox
import time
import random

from dropbox.oauth import TOKEN_ACCESS_TYPES
start_time=time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="image"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("SnapShotTaken")    
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    

def upload_file(image_name):
        access_token="ZOEl8pcyEvIAAAAAAAAAARrOPZaUyE8wRaMeHNqkgXhsGcgm0_FwEl7fWVqtk1oj"
        file=image_name
        file_from=file
        file_to="/test/"+(image_name)
        dbx=dropbox.Dropbox(access_token)
        with open(file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
            print("files uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)         
main()       