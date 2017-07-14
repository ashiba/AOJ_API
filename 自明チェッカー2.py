# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib2

ME="yazaten"
solvedMembers=10

solvedActiveMembers=5

userList=[
	"Respect2D","kioa","yokit9","ik11235","utisam","0lbBaka","nkkwe","KNKedge","slip0110",
	"komi0222","menphim","ja3rno","dispenser","arsenic28","ayihis","fukku",
	"bnsgny","CROW","is0220rk","okkyun","tmbsx","yazaten",
	"is0248vx","Nanana","satoshi31043","mots555","ixmel","pikanatsu","kerokero","futo","proru","sarada417","is0268ev","IS0283IR","moon_remon","kinono","is0266hx","Rp7rf"
]

activeList=[
           "komi0222","menphim","ja3rno","dispenser","arsenic28","ayihis","fukku",
           "bnsgny","CROW","is0220rk","okkyun","tmbsx","yazaten",
           "is0248vx","Nanana","satoshi31043","mots555","ixmel","pikanatsu","kerokero","futo","proru","sarada417","is0268ev","IS0283IR","moon_remon","kinono","is0266hx","Rp7rf"
]


def getUser(id):
    response = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
    return response



def getSolvedList(id,Dict):
	html=getUser(id)
	#
	tree=ET.parse(html)
	root=tree.getroot()
	#
	for problemNum in root.findall(".//problem/id"):
		Dict[problemNum.text]+=1;
	#
	return Dict



solvedDict=defaultdict(lambda : 0)
solvedActiveDict=defaultdict(lambda : 0)
solvedMeDict=defaultdict(lambda : 0)

solvedMeDict=getSolvedList(ME,solvedMeDict);

for name in userList:
    solvedDict=getSolvedList(name,solvedDict)

for name in activeList:
    solvedActiveDict=getSolvedList(name,solvedActiveDict)


toSolveList=[]
for problemNum in solvedDict:
    if solvedDict[problemNum]>=solvedMembers:
        toSolveList.append(problemNum)

for problemNum in solvedActiveDict:
    if solvedActiveDict[problemNum]>=solvedActiveMembers:
        toSolveList.append(problemNum)

toSolveList=list(set(toSolveList));
toSolveList=sorted(toSolveList)

print "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=\"utf-8\">\n\t\t<title>problems</title>\n\t</head>\n\t<body>"

count=0
for problemNum in toSolveList:
	if solvedMeDict[problemNum]==0:
		count+=1
		print "\t\t<a href="+"http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id="+problemNum+"&lang=jp"+">"+problemNum+"</a>　"
		if count%15==0 :
			print "\t\t<br><br>"

print "\t</body>\n</html>"
