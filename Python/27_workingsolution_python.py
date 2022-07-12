
# [ Edited On 16.2.2016 ] 
# On that date this program was working. 

#Warning: For original Bucky's typed lines of code, take a look at the file 27_python.py .

#Description:
#This file is alternative solution for web crowler. 
# Mayor reason for this is that website BuckysRoom.com is down, so original code doesnot work anymore. 
# Solution description (what this program does):
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
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text,'html.parser')
        for link in soup.findAll('a', {'class': 'user-name'}):
            href = link.get('href')
            title = link.string  # just the text, not the HTML
            print(href)
            print(title)
            #get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    # if you want to gather photos from that user
    for item_name in soup.findAll('img', {'class': 'img-responsive'}): # all photos of the user
        photo='https://thenewboston.com'+item_name.get('src')
        print(photo)
    # if you want to gather links for a web crawler
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)


trade_spider(1)




