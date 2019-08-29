# for this to work, you need to allow "less secure apps" to access your google account:
# 		https://support.google.com/accounts/answer/6010255
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email='xx@clemson.edu'
my_password=''

# probably want to read these out of a csv next time
params=[
{"class":"ECE4720-001", "professor":'xx', "email_address":'xx@clemson.edu'},
{"class":"ECE4090-001", "professor":'xx', "email_address":'xx@clemson.edu'},
{"class":"ECE4420-001", "professor":'xx', "email_address":'xx@clemson.edu'},
{"class":"ECE4950-001", "professor":'xx', "email_address":'xx@clemson.edu'},
{"class":"ECE3720-001", "professor":'xx', "email_address":'xx@clemson.edu'},
{"class":"Rifle Class", "professor":'xx', "email_address":'xx@clemson.edu'}
]

try:
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
my_password=''
	for p in params:
		to_email=p['email_address']
		cc = 'xx@clemson.edu'
		subject=p['class']+": Scheduled Absences"
		body="Hello "+p['professor']+',\n'+\
		"""
This semester I am doing undergraduate research for xx and am also the Treasurer of Tau Beta Pi. Due to these obligations, I will have to leave the state of south carolina to attend 3 separate conferences:

	The first conference I will be attending is IEEE Cluster 2019 in Albuquerque, New Mexico to present a research paper. This conference will be from September 23-26, requiring me to miss a full week of class.
	The second conference is the Tau Beta Pi convention in Colombus, Ohio on October 10-11, requiring me to miss Wednesday October 9th through Friday October 11th.
	The last conference I will be required to attend is SC19 in Denver, Colorado, where I will be a student volunteer and potentially be presenting a research poster (awaiting poster acceptance). This conference is from November 18-22, requiring me to miss a full week of class.

I believe that I may be able to miss part of IEEE Cluster 2019, only attending the day of my presentation (and possibly an additional 2 days for travel), but I am not yet certain about this. Is there anything you need from me in advance, so that I can be sure that these absences do not negatively impact my grade?
		
Best Regards,
Pavlo Triantafyllides
		"""
		msg = MIMEMultipart()
		msg['From']=my_email
		msg['To']=to_email
		msg['Cc']=cc
		msg['Subject']=subject
		msg.attach(MIMEText(body,'plain'))
		server.send_message(msg)
		del msg
		#server.sendmail(my_email, to_email, body)

	server.close()
	print('DONE')

except Exception as e:
	print("FAILED: "+str(e))


