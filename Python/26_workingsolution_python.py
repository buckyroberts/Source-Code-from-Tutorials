# [ Edited On 16.2.2016 ]
# On that date this program was working.

#Warning: For original Bucky's typed lines of code, take a look at the file 26_python.py .

#Description:
#This file is alternative solution for web crowler.
# Mayor reason for this is that website BuckysRoom.com is down, so original code doesnot work anymore.
#
# Solution description (what this actually program does - not the same as in the video):
#This program goes on website https://www.thenewboston.com/search.php?type=0&sort=reputation ,
#and goes on every user's profile, and on that profile, 
#it prints the first few (approx. 20) links of latest photos. To view photos, click on url or copy in web broser.


# But history is changing and sooner or later this file or program will not work!.
# On day of the creation this program was working.






import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'https://thenewboston.com/search.php?type=0&sort=reputation&page==' + str(page)
		source_code = requests.get(url, allow_redirects=False)
		plain_text = source_code.text.encode('ascii', 'replace')
		soup = BeautifulSoup(plain_text,'html.parser')
		for link in soup.findAll('a', {'class': 'user-name'}):
			href = link.get('href')
			title = link.string
			print(href)
			print(title)
		page += 1

trade_spider(1)
