# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib2

ME="Yazaten"

def getUser(id):
    response = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
    return response


def makeUserData():
	html=getUser(ME);
	#
	tree=ET.parse(html)
	root=tree.getroot()
	#
	#
	return root

userData = makeUserData()


probDict = defaultdict(lambda:False)
c = 0
probList=[]
for prob in open('prob.txt','r'):
	prob = prob[:-1]
	probDict[prob] = False
	probList.append(prob)
	c+=1
for num in userData.findall(".//problem//id"):
	if c==0: break
	for prob in probDict:
		if num.text==prob:
			probDict[prob]=True
			c-=1

for prob in probList:
	str=""
	if probDict[prob]==True:
		str="Solved"
	else:
		str="Un solved"
	print prob+" : "+str

