import subprocess
import admin
import os
import sys

def getData():
	try:
		cmd = ['C:\\Projects\\fsTools\\MftRcrd-master\\MFTRCRD.exe', 'C:\\Projects\\test2.py', '-d', 'indxdump=off', '1024', '-s']
		p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
		out, err = p1.communicate()
		result = out.decode()
		print result
		#output = p1.communicate()[0]
		#subprocess.check_call(['C:\\Projects\\fsTools\\MftRcrd-master\\MFTRCRD.exe', 'C:\\Projects\\test2.py', '-d', 'indxdump=off', '1024', '-s'])
		f = open('admin.txt','w')
		f.write('ran MFTRCRD.exe: ' + result)
		f.close()
	except:
		try:
			f = open('admin.txt','w')
			f.write('ran PLASO')
			f.close()
		except:
			f = open('admin.txt','w')
			f.write('failed to run either')
			f.close()


#if not admin.isUserAdmin():
	#admin.runAsAdmin(getData())

	

rc = 0
if not admin.isUserAdmin():
	print "You're not an admin.", os.getpid(), "params: ", sys.argv
	#rc = runAsAdmin(["c:\\Windows\\notepad.exe"])
	rc = admin.runAsAdmin()
else:
	print "You are an admin!", os.getpid(), "params: ", sys.argv
	rc = 0
	getData()

	
"""
import admin
import os
import subprocess

if not admin.isUserAdmin():
	try:
		admin.runAsAdmin()
		
		subprocess.call(['C:\\Projects\\fsTools\\MftRcrd-master\\MFTRCRD.exe', 'C:\\Projects\\test2.py', '-d', 'indxdump=off', '1024', '-s'])
		
		f = open('admin.txt','w')
		f.write('ran MFTRCRD.exe')
		f.close()
	except:
		f = open('admin.txt','w')
		f.write('run PLASO')
		f.close()
"""