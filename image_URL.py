import requests
from bs4 import BeautifulSoup

def make(ref: str) -> str:
    domain = "https://bersoantik.com"
    itemUrl = '{}/catalog/article/{}/'.format(domain, ref)

    r = requests.get(itemUrl)
    soup = BeautifulSoup(r.text, 'lxml')

    end = soup.find('div', class_="swiper-zoom-container").find('img', class_="object_slide").get('src')

    return domain + end
