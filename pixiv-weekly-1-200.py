from BeautifulSoup import BeautifulSoup
import urllib2,urllib,os,time

year = time.strftime('%Y',time.localtime(time.time()))
month = time.strftime('%m',time.localtime(time.time()))
day = time.strftime('%d',time.localtime(time.time()))
folder_time = year+'-'+month+'-'+day

n_page = 5
for n in range(1,n_page):
    n1 = str(n)
    url = 'http://www.pixiv.net/ranking.php?mode=weekly&content=illust&p='+n1
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    a = soup.findAll('a','image-thumbnail')
    a_num = len(a)
    imgs = soup.findAll('a','image-thumbnail')
    for i in range(0,a_num):
        imgurl = imgs[i].find('img')['data-src']
        imgurl = imgurl.replace('?ctype=ranking','')
        imgurl = imgurl.replace('_s','')
        file=open('pixiv-weekly-1-200-'+folder_time+'.txt','a')
        file.writelines(imgurl)
        file.writelines('\n')
        file.close()
