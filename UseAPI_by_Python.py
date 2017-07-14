# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET	#xmlを木構造にして色々するやつ
import urllib2						#URLからxmlを取得するやつ


def getXmlData(id):
    xml = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
    return xml


def getRootData(xml):
    tree=ET.parse(xml)
    root=tree.getroot()
    
    return root


#xmlデータを取得
xml=getXmlData("yazaten")

#xmlデータをElementTreeで木構造に変換
root=getRootData(xml)



#solved数を出力
print "solved : "+root.find(".//solved").text


#解いた全ての問題番号のリストをproblemNumbersに入れる
problemNumbers=root.findall(".//problem/id")

#問題番号を1つずつ出力
for number in problemNumbers:
	print number.text