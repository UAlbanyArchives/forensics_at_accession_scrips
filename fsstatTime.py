import os
import time
import bagit
import subprocess

#function written by Fred Cirera: http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


path = "C:\\Projects\\testing\\testData"



timeTotal1 = time.time()

subprocess.call(['C:\\Projects\\fsTools\\sleuthkit-4.1.3-win32\\bin\\fsstat.exe', '\\\.\c:'])
	
timeTotal2 = time.time()

totalTime = timeTotal2 - timeTotal1

print totalTime