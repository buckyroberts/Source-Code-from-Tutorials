import requests
from b4 import BeautifulSoup


def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class': 'item-name'}):
        href = "https://buckysroom.org" + link.get('href')
        title = link.string
        print(href)
        print(title)
    page += 1
    
trade_spider(1)
