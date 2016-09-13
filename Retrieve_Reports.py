#coding=utf-8
import urllib
import re
f='/Users/TJX/Documents/python exp/pics/'

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getPdf(html):
    reg=r'href="(.+?\.pdf)"'
    pdfre=re.compile(reg)
    pdfList=re.findall(pdfre,html)
    print pdfList,len(pdfList)
    prefix='http://cs231n.stanford.edu/reports2016/'
    for pdf in pdfList:
        urllib.urlretrieve(prefix+pdf,f+pdf)
url='http://cs231n.stanford.edu/reports2016/'
html=getHtml(url)
getPdf(html)


