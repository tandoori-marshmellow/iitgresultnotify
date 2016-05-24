import urllib2
import time
import os
from bs4 import BeautifulSoup
import urllib2
import cookielib
import sys

username = "your username" #username on way2sms
passwd = "your password" #password on way2sms
message = "message to be sent (max. 130 char)" #message
number = "phone number on which message is to be sent" #your phone number
message = "+".join(message.split(' '))

url = 'https://www.iitg.ernet.in/acad/gradespicpi/home'

while True:

	htm = urllib2.urlopen(url).read()
	soup = BeautifulSoup(htm,'html.parser')
	xyz = soup.find_all('small')
	for i in xyz:
		d = i.text
	req = unicode('Last updated:  25 May 2016') #update date to the day results are to be declared
	if req==d:
		os.system("notify-send 'results out bitch! go sleep.'")
		#Logging into the SMS Site
		url = 'http://site24.way2sms.com/Login1.action?'
		data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
		 
		#For Cookies:
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		 
		# Adding Header detail:
		opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
		 
		try:
		    usock = opener.open(url, data)
		except IOError:
		    print "Error while logging in."
		    sys.exit(1)
		 
		 
		jession_id = str(cj).split('~')[1].split(' ')[0]
		send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
		send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
		opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
		 
		try:
		    sms_sent_page = opener.open(send_sms_url,send_sms_data)
		except IOError:
		    print "Error while sending message"
		
		break;
		print "SMS has been sent."
	time.sleep(60)


