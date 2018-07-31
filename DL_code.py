# -*- coding: utf-8 -*-
# あるユーザがAOJに提出した全コード(?)を保存する


from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib.request

ME="Yazaten"
judgeURL = "http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid="

def getUser(id):
	response = urllib.request.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
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
	page = page.replace( b'&lt;'	,	b'<' )
	page = page.replace( b'&gt;'	,	b'>' )
	page = page.replace( b'&quot;',	b'\"')
	page = page.replace( b'&amp;',	b'&')
	page = page.replace( b'&nbsp;',	b' ')
	page = page.replace( b'                  <pre class=\"brush: cpp\" name=\"code\" id=\"code\">', b'' )
	page = page[:-1]
	return page


problemList = getSolvedList(ME)

for i,problem in enumerate(problemList):
	problemid = problem[0]
	judgeid = problem[1]
	html = urllib.request.urlopen( judgeURL+str(judgeid) )

	list = []
	flag = False
	for page in html:
		if page.count( b'#include' ):
			flag = True
		if flag == True:
			if page.count( b'</pre>\n' ):
				break
			else :
				page = format( page )
				list.append(page)

	f = open(str(problemid)+'.cpp', 'w') # 書き込みモードで開く
	for line in list:
		f.write( line.decode('utf-8')+'\n' ) # 引数の文字列をファイルに書き込む
	f.close() # ファイルを閉じる
