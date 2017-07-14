# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib2

allList=[
#	"Respect2D","kioa","yokit9","ik11235","utisam","0lbBaka","nkkwe","KNKedge","slip0110",
	"komi0222","menphim","dispenser","arsenic28",
	"CROW","yazaten",
	"is0248vx","ixmel","futo","is0268ev","IS0283IR","moon_remon","is0266hx"
#	"yazaten","IS0283IR","ixmel"
]

userList=[
	"Taka13","noy72","is0310ph","moon_remon"
]


def getUser(id):
    response = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
    return response


def makeUserDataDict(list):
	userDataDict=defaultdict(lambda : 0)
	#
	for id in list:
		html=getUser(id);
		#
		tree=ET.parse(html)
		root=tree.getroot()
		#
		userDataDict[id]=root
	#
	return userDataDict

probDict = defaultdict(lambda:0)

allUserDict=makeUserDataDict(allList)

t=len(userList)
for name in allList:
	for prob in allUserDict[name].findall(".//problem"):
		probDict[prob.find(".//id").text]+=(2**t)
	t+=1


userDataDict=makeUserDataDict(userList)
c=0
for name in userList:
	for prob in userDataDict[name].findall(".//problem"):
		probDict[prob.find(".//id").text]+=(2**c)
	c+=1

list=[]
for prob in probDict:
	list.append( (prob,probDict[prob]) )

list = sorted(list,key=lambda x:x[0],reverse=False)
list = sorted(list,key=lambda x:x[1],reverse=False)

#for data in list:
#	if data[1]==0:
#		print data[0]
for data in list:
	if data[1]%(2**len(userList))==0:
		print data[0]
#		if  (data[1]/(2**len(userList))) == 2**len(allList)-1 :
#			print data[0]