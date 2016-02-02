#coding=utf-8
import  xml.dom.minidom
import os
os.system("nmap -vv -p80,443,8080 --open -Pn  -iL ln.txt -oX ln.xml")#执行Nmap命令
#命令解释
#-vv 详细输出
#-p  指定端口扫描，这里指定80，443,8080三个常见的端口
#--open 仅输出开放的端口
#-Pn  不是用ping探测，运营商网络可能会禁ping，导致扫描时间长而且不准确
#-iL  指定扫描的地址列表文件
#-oX  结果输出为xml类型
####################################################################################
#使用Python标准库中的xml.dom.minidom处理XML文件
dom = xml.dom.minidom.parse('ln.xml')#打开xml文档
root = dom.documentElement#得到文档元素对象
host_nodes= root.getElementsByTagName('host')
file=open('ln_web.txt','a')#创建输出文件
for host in host_nodes:
    addlist=host.getElementsByTagName("address")
    add=addlist[0]
    ip=add.getAttribute("addr")
    portlist=host.getElementsByTagName("port")
    for port in portlist:
        P= port.getAttribute("portid")
        if P=="80":
            url1="http://"+ip   # 80端口则加上协议前缀http://
            file.write(url1+'\n')
        elif P=="8080":
            url2="http://"+ip+":8080"#8080端口则加上前缀http://并指定端口8080
            file.write(url2+'\n')
        else:
            url3= "https://"+ip#433端口则加上https://
            file.write(url3+'\n')#将处理后的结果写入文件
file.close()






