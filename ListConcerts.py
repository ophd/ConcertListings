import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.inertia-entertainment.com/',
                    # headers={'User-Agent': 'Mozilla/5.0'})
                    headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# http = HTTPSession()
# page = http.request('get', 'https://www.inertia-entertainment.com/')

soup = BeautifulSoup(page.text, 'html.parser')

events_list = soup.find('ul', {'class': 'eventsList'})

for li in events_list.find_all('li'):
    name = li.find('h3').text.strip()
    date = li.find('p', {'class':'date'}).text.strip()
    time = li.find('p', {'class':'time'}).text.strip()
    venue = li.find('p', {'class':'venue'}).text.strip()
    print(f'{name}\t{date}\t{venue}')