import requests
from b4 import BeautifulSoup


def trade_spider(max_pages):
  page = 1
  while page < max_page:
    url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
    source_code = requests.get(url)
    plain_text = 