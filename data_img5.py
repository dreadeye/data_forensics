import struct
import sys
ipath="/Users/nido/Desktop/limerick/spring/ee6012-data forensics/Sample_1 Image/Sample_1.dd"
#63*512 start of the sector
b=000
c=020
print b,c
li=[b,c] #offset location to seek
toread=512 # size to be read-otherwise memory error
with open(ipath,'rb') as fi:
	print "name=",fi.name
	for a in li:
		fi.read(toread)
		print fi.seek(a)
		toread+=toread+512
		print toread
		print fi.readline().strip(),"\n"
fi.close()
