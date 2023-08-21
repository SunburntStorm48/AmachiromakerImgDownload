import urllib.request
import time
import os
imglist = [

]
#list of files
urlprefix = 'https://cdn.picrew.me/app/image_maker/'
prefix = 'C:/Downloads/pytemp/'
despath = 'C:/Downloads/pytemp/168503/' #path to save the files
if os.path.exists(prefix) == False:
    os.mkdir(prefix)
if os.path.exists(despath) == False:    
    os.mkdir(despath)

for i in imglist:
    url = urlprefix + i
    files = prefix + i
    urlx = str(url)
    filesx = str(files)
    
    string = i
    string = string[0:13]
    ipath = prefix + string
    
    print (ipath)
    if os.path.exists(ipath) == False:
        os.mkdir(ipath)
    urllib.request.urlretrieve(urlx, filesx)
    print('Downloaded', urlx)
    print('Saved', filesx)
