import requests
from bs4 import BeautifulSoup

r = requests.get('https://divar.ir/s/tehran/jobs?q=%5C')

soup = BeautifulSoup(r.text,'html.parser')


ads = soup.find_all("div", attrs={'class':'kt-post-card__body'})

for item in ads:
    title = item.find('h2',attrs= {'class':'kt-post-card__title'})
    desc = item.find('div', attrs={'class':'kt-post-card__description'})
    if title and desc:
        title= title.text.strip()
        desc=desc.text.strip()

        if 'توافقی'in desc:
            print (title)
            
