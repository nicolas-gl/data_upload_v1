import requests
from bs4 import BeautifulSoup

domain = "https://bersoantik.com"
ref = "02_0736"

itemUrl = '{}/catalog/article/{}/'.format(domain, ref)


r = requests.get(itemUrl)
soup = BeautifulSoup(r.text, 'lxml')

end = soup.find('div', class_="swiper-zoom-container").find('img', class_="object_slide").get('src')

imgUrl = domain + end
print(imgUrl)
