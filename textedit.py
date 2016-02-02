#coding=utf-8
f=open('wz.txt')#打开读取文件
file=open('result.txt','a')#打开写入的文件
while 1:
    line=f.readline()#读取一行
    if not line:
        break
    p=line.split(';')
    for name in p:
        if name!='\n':
            url="http://www."+name
            print url
            file.write(url+'\n')
f.close()
file.close()




