import urllib.request
import time
import os
import sys
imglist = [

]
#list of files
urlprefix = 'https://cdn.picrew.me/app/image_maker/'
prefix = 'C:/Downloads/pytemp/'
despath = 'C:/Downloads/pytemp/168503/' #path to save the files
length = len(imglist)
m = 0
k = 0

if os.path.exists(prefix) == False:
    os.mkdir(prefix)
if os.path.exists(despath) == False:    
    os.mkdir(despath)

def down(i):
    url = urlprefix + i
    files = prefix + i
    urlx = str(url)
    filesx = str(files)
    
    string = i
    string = string[0:13]
    ipath = prefix + string

    if os.path.exists(ipath) == False:
        os.mkdir(ipath)
    urllib.request.urlretrieve(urlx, filesx)

print ('[Downloading', length, 'files]')

for i in imglist:
    down(i)
    m += 1
    k = int((m / length) * 100)

    kp = k // 2
    print('\r', end='')
    print('Download progress: {}% |'.format(k), '█' * kp, '--' * (50 - kp),'|', m,'/',length, end='')
    sys.stdout.flush()

print ('[Downloaded', length, 'files]')
