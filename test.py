import urllib.request
from bs4 import BeautifulSoup
import time

t = time.localtime()
time_now = time.strftime("%y/%m/%d, %H:%M:%S", t)



with open('/home/ucare/CONVID-19_time.txt', 'a+') as f:
	pass

urlStr = "https://www.cdc.gov.tw/En"

fileObj = urllib.request.urlopen(urlStr)

soup = BeautifulSoup(fileObj, 'html.parser')


all_tag = soup.find_all(class_="content-boxes-in-v3")

all_tag = str(all_tag[0])

for i in range(len(all_tag)):
	if all_tag[i:i+4] == "CECC":
		today_conformed_cases_information = all_tag[i:]	

today_conformed_cases_information = today_conformed_cases_information.split(";")[0]


time = str(soup.find_all(class_="EmbedTime")[0])[21:].split("<")[0]

with open('/home/ucare/CONVID-19_time.txt', 'r+') as f:
	lines = f.read().splitlines()
	if len(lines) == 0:
		f.writelines(time_now + " : " + time + "\n")
		print(today_conformed_cases_information + " since last update ")
	else:
		if lines[-1].split(" : ")[1] != time:
			print(today_conformed_cases_information + " since last update " + lines[-1].split(" : ")[1] + ".")
		else:
			print("Confirmed cases not updated yet")
		f.writelines(time_now + " : " + time + "\n")




