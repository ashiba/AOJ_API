# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import datetime
import urllib2
import time
import sys

ME="ixmel"
CHECK_DAY=3

def getUserData(id):
    xml = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
	#
    tree=ET.parse(xml)
    root=tree.getroot()
    #
    return root



root= getUserData(ME)
d = datetime.datetime.today()

#今日の夜24:00のUNIX秒
now = int(time.time()) - (d.hour*60*60 + d.minute*60 + d.second) + 24*60*60

daySolved=[0]*CHECK_DAY
if( len(root.findall(".//problem/submissiondate"))==0 ):
		for i in range(CHECK_DAY):
			daySolved[i]=-1
else:
	for problem in root.findall(".//problem/submissiondate"):
		if(problem!=None):
			dayBefore=int( (now - int(problem.text[0:len(problem.text)-3])) / (24*60*60) )
			if(dayBefore<CHECK_DAY):
				daySolved[dayBefore]+=1

sys.stdout.write("%12s : " % ME)
for problemSum in daySolved:
	sys.stdout.write("%4d" % problemSum)
print

