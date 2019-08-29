# I used this to clear all the info from SendEmail.py
import re
import sys

#fname = sys.argv[1]
fname = 'SendEmail.py'

lines=[]
with open(fname, 'r+') as f:
	lines=f.readlines()

with open(fname, 'w+') as f:
	for l in lines:

		if 'my_password' in l:
			l = 'my_password=\'\''
		else:
			# delete email addresses
			l = re.sub(r'(\"|\')[A-Za-z0-9\.]+@[A-Za-z0-9\.]+(\"|\')','\'xx@clemson.edu\'',l)
			# delete professor names
			l = re.sub(r'(Dr.|Professor) [A-Za-z]+','xx',l)
		f.write(l)



