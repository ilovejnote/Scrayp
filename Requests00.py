# -*- coding: utf-8 -*-
import requests
r = requests.get("http://www.baidu.com")
r.status_code
r.encoding = 'utf-8'
nettext = r.text
print(nettext)



# common code for scrapy webpage
import requests
def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 5)
		r.raise_for_status() #if status_code != 200 ,then cause HTTPError.
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"


if __name__ == '__main__':
	url = "http://www.baidu.com"
	print(getHTMLText(url))
	