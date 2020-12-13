#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

NAME = ''
PASS = ''
ADDR = ''
UUID = ''

url = 'https://nco.zjgsu.edu.cn/login'
data = {
    'name':NAME,
    'pass':PASS,
}
uuid = 
s = requests.session()
r = s.get(url=url)
print '---------------------------------------------'
zjgsusessionsid = r.cookies.get_dict()['zjgsusessionsid']
print zjgsusessionsid
print '---------------------------------------------'
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36',
    'Origin':'https://nco.zjgsu.edu.cn',
    'Referer':'https://nco.zjgsu.edu.cn/login',
    #'Cookie':'_ncov_uuid={}; zjgsusessionsid={}; _ncov_username={}; _ncov_psswd={}'.format(UUID, zjgsusessionsid, data['name'], data['pass']),
}
print headers
print '---------------------------------------------'
r = s.post(url=url, data=data, headers=headers)
print r.text
print '---------------------------------------------'

url = 'https://nco.zjgsu.edu.cn/'
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36',
    'Cookie':'_ncov_uuid={}; zjgsusessionsid={}; _ncov_username={}; _ncov_psswd={}'.format(UUID, zjgsusessionsid, data['name'], data['pass']),
    'Origin':'https://nco.zjgsu.edu.cn',
    'Referer':'https://nco.zjgsu.edu.cn/',
}
r = s.get(url=url, headers=headers)
print r.text
print '---------------------------------------------'
data = {
    'uuid':UUID,
    'currentResd':ADDR,
    'fromHbToZjDate':'',
    'fromHbToZj':'C',
    'fromWtToHzDate':'',
    'fromWtToHz':'B',
    'meetDate':'',
    'meetCase':'C',
    'travelDate':'',
    'travelCase':'D',
    'medObsvReason':'',
    'medObsv':'B',
    'belowCaseDesc':'',
    'belowCase':'D',
    'temperature':'',
    'notApplyReason':'',
    'hzQRCode':'A',
    'specialDesc':'',
}
print data
print '---------------------------------------------'
r = s.post(url=url, headers=headers, data=data)
print r.headers
print '---------------------------------------------'
c = r.text
print c
print '---------------------------------------------'
t = time.ctime()
isDone = False
if '当天只能申报一次!' in c:
    isDone = True
    c = '当天只能申报一次!'
else:
    c = '报送成功！'
with open('log', 'ab+') as f:
    f.write('---------------------------------------------\n')
    f.write(t + '\n')
    f.write(c.encode('utf-8') + '\n')
    f.write('---------------------------------------------\n')
print c
print '---------------------------------------------'

if isDone:
    print '[!] Already punched.'
    exit(0)

print '[+] Done'
