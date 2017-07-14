# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib2

ME="yazaten"
solvedMembers=10

userList=[
	"Respect2D","kioa","yokit9","ik11235","utisam","0lbBaka","nkkwe","KNKedge","slip0110",
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



userDataDict=makeUserDataDict()


rankList=[]

for name in userList:
	userTree=userDataDict[name]
	if( userTree.find(".//solved")!=None ):
		rankList.append(( name , int(userTree.find(".//solved").text)) )
	else:
		rankList.append( (name,int(-1))	)	


rankList.sort(key=lambda x:x[1], reverse=True)


num=1;
for data in rankList:
	print str(num)+" : "+data[0]+"\t"+str(data[1])
	num+=1



