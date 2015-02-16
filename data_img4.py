'''


from functools import partial
import shutil #copies the file with the specified block size to a new image disk file
ipath="/Users/nido/Desktop/limerick/spring/ee6012-data forensics/Sample_1 Image/Sample_1.dd"
iwrite="/Users/nido/Desktop/limerick/spring/ee6012-data forensics/Sample_1 Image/Sample_2.dd"
blocksize = 4
with open(ipath, 'rb') as f, open(iwrite, 'wb') as dest:
    shutil.copyfileobj(f, dest, blocksize)

'''


ipath="/Users/nido/Desktop/limerick/spring/ee6012-data forensics/Sample_1 Image/Sample_1.dd"
ipath2="/Users/nido/Desktop/limerick/spring/ee6012-data forensics/Sample_1 Image/Sample_3.dd"
with open(ipath,'rb') as f:
    with open(ipath2, "wb") as i:
        while True:
            if i.write(f.read(512)) == 0:
                break
print i.read()                