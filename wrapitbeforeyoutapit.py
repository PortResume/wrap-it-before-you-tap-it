import requests
import time 

#written by The DisgruntledVet

#Do you have muliple domains that you own or want to check multiple url links for viruses, worms, trojans and other kinds of malicious content look no further wrapitbeforeyoutapit is here 
#All you need to do is sign up for free on virus total to recieve a public api key here https://www.virustotal.com/en/documentation/public-api/
#once you recieve it you can copy and paste my code and add your key in in appropriate spots marked your api key
#next add what links/urls need to be checked in links.
#next run the script in your terminal by using py wrapitbeforeyoutapit.py
#any questions email me at whatthehacknews@gmail.com
print ('---------------------------------')
print ('|                                |')
print ('|                                |')
print ('|      WRAP IT BEFORE YOU        |')
print ('|           TAP IT.              |')
print ('|                                |')
print ('---------------------------------')





def lets_send_it():
	#virus totals api url
	url = 'https://www.virustotal.com/vtapi/v2/url/scan'
	#params is your key what is a api key it is essentially a password ro be able to use the api. 
    #url calls links which links is all the urls we want to check.
	params = {'apikey': '', 'url': links}
	#posts the url that you want to be checked 
	response = requests.post(url, params=params)


	print(response.text)


def give_me_that():
	url = 'https://www.virustotal.com/vtapi/v2/url/report'

	params = {'apikey': '', 'resource': links}
	#grabs the report for the url you posted 
	response = requests.get(url, params=params)


	#prints report in terminal
	print(response.text)

	json_response = response.json()
	#calling specific information from json. 
	#when a json is printed off it looks like a bunch of commas and charachters 
	#this will allow you to read the information you want to see 
	url = json_response["url"]
	scan_date = json_response["scan_date"]
	positives = json_response["positives"]
	total = json_response["total"]
	#markdown learn about here it here https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
	#Markdown is a lightweight markup language with plain text formatting syntax. Its design allows it to be converted to many output formats
	md = """
	# Scan Results

	### URL: {url}
	### SCAN DATE: {scan_date}
	### POSITIVES: {positives}
	###TOTAL: {total}
	""" .format(url=url, scan_date=scan_date, positives=positives, total=total)
	#scans = json_response['scans']
	scanners = json_response["scans"].keys()
	md += """

	| Scanner        | Detected           | Result  |
	| ------------- |:-------------:| -----:|
	"""
	for scanner in scanners:
		detected = json_response["scans"][scanner]["detected"]
		result = json_response["scans"][scanner]["result"]
		md += """|{scanner}| {detected}| {result}|\n""".format(scanner=scanner, detected=detected, result=result)
	#creating file Results.md 
	with open("Results.md", "w") as fileObject:
		fileObject.write(md)
	




#urls/links  you want to be checked 
links = ['http://myportresume.com/'
		 ]


for url in links:   
   page = requests.get(url)

   #this if statement states if page not found it will not post url  or get reports
   if  page.status_code == 404 or page.url == 'https://twitter.com/account/suspended':
   	   print( 'gotem', page.url)
   	   
   	  

   #this else statement posts url and gets report if status code is anything but 404 there will be a 15sec time lapse 
   else: 
         
   		print ('still up', page.url)
   		lets_send_it()
   		print ('...........................grabbing report...............................')
   		#you must sleep a few seconds to give the report time to run 
   		time.sleep(15)
   		give_me_that()
   		print ('...........................posting URL..................................')
		time.sleep(5)

   

   		#webbrowser.open(page.url)
