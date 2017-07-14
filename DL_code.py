# -*- coding: utf-8 -*-

from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib2

ME="yazaten"
judgeURL = "http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid="

def getUser(id):
    response = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
    return response



def getSolvedList(id):
	list = []
	html=getUser(id)
	#
	tree=ET.parse(html)
	root=tree.getroot()
	#
	a = []
	b = []
	for problemid in root.findall(".//problem/id"):
		a.append( problemid.text )
	for judgeid in root.findall(".//problem/judge_id"):
		b.append( judgeid.text )
	#
	for i in range(len(a)):
		list.append( (a[i],b[i]) )
	return list



def format( page ):
	page = page.replace( "&lt;"	,	"<" )
	page = page.replace( "&gt;"	,	">" )
	page = page.replace( "&quot;",	"\"")
	page = page.replace( "&amp;",	"&")
	page = page.replace( "&nbsp;",	" ")
	page = page.replace( "                  <pre class=\"brush: cpp\" name=\"code\" id=\"code\">", "" )
	page = page[:-1]
	return page


problemList = getSolvedList(ME)

for i,problem in enumerate(problemList):
	if i==3:break
	problemid = problem[0]
	judgeid = problem[1]
	html = urllib2.urlopen( judgeURL+str(judgeid) )

	list = []
	flag = False
	for page in html:
		if page.count( "#include" ):
			flag = True
		if flag == True:
			if page.count("</pre>\n"):
				break
			else :
				page = format( page )
				list.append(page)

	f = open(str(problemid)+".cpp", 'w') # 書き込みモードで開く
	for line in list:
		f.write(line+"\n") # 引数の文字列をファイルに書き込む
	f.close() # ファイルを閉じる
