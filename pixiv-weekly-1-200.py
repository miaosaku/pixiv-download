# -*- coding: utf8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2,urllib,os,time
import cookielib

year = time.strftime('%Y',time.localtime(time.time()))
month = time.strftime('%m',time.localtime(time.time()))
day = time.strftime('%d',time.localtime(time.time()))
folder_time = year+'-'+month+'-'+day

logindata={'mode':'login', 'pixiv_id':'hm00com@gmail.com', 'pass':'a'}

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar()))
data = urllib.urlencode(logindata)

f = opener.open('http://www.pixiv.net/login.php', data)
if f.read().find('pixiv.user.loggedIn = true') != -1:
    v =  'vv'
    print u'登录成功'

else:
    v =  'xx'
    print u'登录失败'
    
n_page = 25
for n in range(1,n_page):
    n1 = str(n)
    url = 'http://touch.pixiv.net/ranking.php?mode=weekly&content=illust&p='+n1
    print url
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    a = soup.findAll('div','imgbox')
    a_num = len(a)
##    print a
    print a_num
    
    for i in range(0,a_num):
        imgurl = a[i].find('a')['href']
        imgurl = imgurl.replace('/member','http://touch.pixiv.net/member')
        imgurl = imgurl.replace('&uarea=daily','')
        imgurl2 = imgurl.replace('medium','big')
        print imgurl2

        req = urllib2.Request(imgurl2, data)
        req.add_header('Referer', imgurl)
        
        html_src = opener.open(req).read()
        parser = BeautifulSoup(html_src)
        imgurl3 = parser.find('img')['src']
        print imgurl3

        file=open('E:\kuaipan\picdowndir\pixiv-weekly-1-200-'+folder_time+v+'.txt','a')
        file.writelines(imgurl3)
        file.writelines('\n')
        file.close()
