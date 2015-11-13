import subprocess
import os
import time

#function written by Fred Cirera: http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


path = "C:\\Projects\\testing\\testData"

fd = open('mftrcrdResults.csv', 'wb')
firstLine = "File Extension" + "," + "Size (Bytes)" + "," + "Size (human readable)" + "," + "Time to run MFTRcrd.exe in seconds" + "\n"
fd.write(firstLine)

timeTotal1 = time.time()

for file in os.listdir(path):
	fullPath = path + "\\" + file
	
	timeFile1 = time.time()
	subprocess.call(['C:\\Projects\\fsTools\\MftRcrd\\MFTRCRD.exe', fullPath, '-d', 'indxdump=off', '1024', '-s'])
	timeFile2 = time.time()
	
	processTime = timeFile2 - timeFile1
	
	ext = os.path.splitext(file)[1]
	fileSize = os.path.getsize(fullPath)
	readFS = sizeof_fmt(fileSize)
	
	newRow = ext + "," + str(fileSize) + "," + readFS + "," + str(processTime) + "\n"
	fd.write(newRow)
	
timeTotal2 = time.time()

totalTime = timeTotal2 - timeTotal1

fd.write(str(totalTime) + "," + "total seconds to process 25 files")

fd.close()