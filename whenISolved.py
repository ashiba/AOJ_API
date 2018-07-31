# -*- coding: utf-8 -*-

#直近CHECK_DAY日のそれぞれのAC数を出力

from collections import defaultdict
import xml.etree.ElementTree as ET
import datetime
import urllib2
import time
import sys

CHECK_DAY=20

userList=[
	"Respect2D","kioa","yokit9","ik11235","utisam","0lbBaka","nkkwe","KNKedge","slip0110",
	"komi0222","menphim","ja3rno","dispenser","arsenic28","ayihis","fukku",
	"bnsgny","CROW","is0220rk","okkyun","tmbsx","yazaten",
	"is0248vx","Nanana","satoshi31043","mots555","ixmel","pikanatsu","kerokero","futo","proru","sarada417","is0268ev","IS0283IR","moon_remon","kinono","is0266hx","Rp7rf",
]

def getUserData(id):
    xml = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
	#
    tree=ET.parse(xml)
    root=tree.getroot()
    #
    return root


d = datetime.datetime.today()

#今日のの夜24:00のUNIX秒
now = int(time.time()) - (d.hour*60*60 + d.minute*60 + d.second) + 24*60*60

for id in userList:
	daySolved=[0]*CHECK_DAY
	root= getUserData(id)
	#
	for problem in root.findall(".//problem/submissiondate"):
		if(problem!=None):
			dayBefore=int( (now - int(problem.text[0:len(problem.text)-3])) / (24*60*60) )
			if(dayBefore<CHECK_DAY):
				daySolved[dayBefore]+=1
	#
	sys.stdout.write("%12s : " % id)
	for problemSum in daySolved:
		sys.stdout.write("%4d" % problemSum)
	print
