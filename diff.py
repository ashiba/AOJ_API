# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import datetime
import urllib2
import time
import sys

ME="yazaten"
USER="IS0283IR"
CHECK_DAY=20

def getUserData(id):
    xml = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
	#
    tree=ET.parse(xml)
    root=tree.getroot()
    #
    return root



root 		= getUserData(ME)
rootDiff 	= getUserData(USER) 

meDict=defaultdict(lambda:0)
userList=[]

for prob in root.findall(".//problem"):
	id = prob.find(".//id").text
	meDict[id]=True

for prob in rootDiff.findall(".//problem"):
	date = prob.find(".//submissiondate").text
	id = prob.find(".//id").text
	userList.append([id,date])

userList = sorted(userList, key=lambda x:x[1], reverse=True)

for data in userList:
	id=data[0]
	if meDict[id]!=True:
		print id
