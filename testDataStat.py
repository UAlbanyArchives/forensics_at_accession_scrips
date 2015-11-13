import os

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

fd = open('testData.csv', 'a')


for fileName in os.listdir("C:\\Projects\\testing\\testData"):
	file = "C:\\Projects\\testing\\testData\\" + fileName
	print file
	ext = os.path.splitext(file)[1]
	fileSize = os.path.getsize(file)
	readFS = sizeof_fmt(fileSize)
	newRow = ext + "," + str(fileSize) + "," + readFS + "\n"
	fd.write(newRow)
fd.close()