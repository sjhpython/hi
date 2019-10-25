import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import time
t1=time.time()
r=requests.get('https://www.tohomh123.com/f-1-15-----updatetime--1.html')
c=r.text
soup=BeautifulSoup(c,'html.parser')

page_div=soup.find('div',{'class':'page-pagination mt20'})


page=page_div.find_all('a')[-2].text

cartoons=[]
urls={'https://www.tohomh123.com/f-1-15-----updatetime--'+str(i)+'.html' for i in range(1,11)}
def crawl_page(url):
    p_r=requests.get(url)
    p_c=p_r.text
    p_soup=BeautifulSoup(p_c,'html.parser')
    p_content=p_soup.find_all('div',{'class':'mh-item'})
    pageCartoon=[]
    for cartoon in p_content:
        carDic={}
        carDic['new']=cartoon.find('div',{'class':'mh-item-detali'}).find('p',{'class':'chapter'}).text
        carDic['text']=cartoon.find('div',{'class':'mh-item-detali'}).find('a').text
        pageCartoon.append(carDic)
    return pageCartoon
pool=mp.Pool()
multi_res=[pool.apply_async(crawl_page,(url,)) for url in urls]
pagesCartoon=[res.get() for res in multi_res]
for pageCartoon in pagesCartoon:
    for cartoon in pageCartoon:
        cartoons.append(cartoon)
print(len(cartoons))
t2=time.time()
print(t2-t1)