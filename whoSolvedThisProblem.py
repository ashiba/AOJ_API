# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib2

ME="yazaten"


userList=[
	"Respect2D","kioa","yokit9","ik11235","utisam","nkkwe","KNKedge","slip0110",
	"komi0222","menphim","ja3rno","dispenser","arsenic28","ayihis","fukku",
	"bnsgny","CROW","is0220rk","okkyun","tmbsx","yazaten",
	"is0248vx","Nanana","satoshi31043","mots555","ixmel","pikanatsu","kerokero","futo","proru","sarada417","is0268ev","IS0283IR","moon_remon","kinono","is0266hx","Rp7rf",
]


def getUser(id):
    response = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
    return response


def makeUserDataDict():
	userDataDict=defaultdict(lambda : 0)
	#
	for id in userList:
		html=getUser(id);
		#
		tree=ET.parse(html)
		root=tree.getroot()
		#
		userDataDict[id]=root
	#
	return userDataDict


def getUnderMeList(rankList):
	retList=[]
	isFoundMe=0
	for id in rankList:
		if isFoundMe==1 :
			retList.append(id)
		#
		if id[0]==ME :
			isFoundMe=1
	#
	return retList



userDataDict=makeUserDataDict()

while True:
	problemNum=input()
	if problemNum==-1 :break
	for name in userList:
		userTree=userDataDict[name]
		for num in userTree.findall(".//problem//id"):
			if(num.text==problemNum):
				print name
				break


