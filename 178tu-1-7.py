from BeautifulSoup import BeautifulSoup
import urllib2,urllib,os,time
import time

year = time.strftime('%Y',time.localtime(time.time()))
month = time.strftime('%m',time.localtime(time.time()))
day = time.strftime('%d',time.localtime(time.time()))
folder_time = year+'-'+month+'-'+day


n_page = 7
for n in range(1,n_page):
    n1 = str(n)
    url = 'http://tu.178.com/picture/hot?_per_page=4&_page_no='+n1
    time.sleep(1)
    print url
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    a = soup.findAll('div','a-img')
    a_num = len(a)
    imgs = soup.findAll('div','a-img')
    for i in range(0,a_num):
        page_url = imgs[i].find('a')['href']
        time.sleep(1)
        print page_url
        page_url = urllib2.urlopen(page_url)
        soup1 = BeautifulSoup(page_url)
        img_url = soup1.findAll('ul','d-box')
        for i in range(0,1):
            imgurl = img_url[i].find('a')['href']
            imgurl = imgurl.replace('?flag=tu178attachment','')
            ##print imgurl
            file=open('178tu-'+folder_time+'.txt','a')
            file.writelines(imgurl)
            file.writelines('\n')
            file.close()
