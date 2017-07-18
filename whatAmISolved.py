# -*- coding: utf-8 -*-
# 直近 CHECK_DAY 日の間に解いた問題のリストを出力する


from collections import defaultdict
import xml.etree.ElementTree as ET
import datetime
import urllib2
import time
import sys

ME="Yazaten"
CHECK_DAY=30

def getUserData(id):
    xml = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
	#
    tree=ET.parse(xml)
    root=tree.getroot()
    #
    return root



root= getUserData(ME)
d = datetime.datetime.today()

#その日の夜24:00のUNIX秒
now = int(time.time()) - (d.hour*60*60 + d.minute*60 + d.second) + 24*60*60

daySolvedList = [[] for i in range(CHECK_DAY)]
for problem in root.findall(".//problem"):
	date = problem.find(".//submissiondate").text
	if(date!=None):
		dayBefore=int( (now - int(date[0:len(date)-3])) / (24*60*60) )
		if(dayBefore<CHECK_DAY):
			daySolvedList[dayBefore].append( problem.find(".//id").text )

print ME
for i,anyDate in enumerate(daySolvedList):
	sys.stdout.write("%3s : " % i)
	for id in anyDate :
		sys.stdout.write("%4s " % id)
	print
