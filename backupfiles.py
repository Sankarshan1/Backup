import os 
import shutil

sour=input ("Enter Source ")
dest=input("Enter Destination")
sour=sour +'/'
dest=dest +'/'
listofallfiles=os.listdir(sour)
for file in listofallfiles:
        shutil.move((sour+file),dest)