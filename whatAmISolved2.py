# -*- coding: utf-8 -*-
# 過去に解いた問題を時系列順に表示する


from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib2
from datetime import *

volumes = [0,1,2,3,5,6,10,15,11,12,13,16,20,21,22,23,24,25,26,27,28]
ME="yurahuna"

def getUserData(id):
    xml = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+id)
	#
    tree=ET.parse(xml)
    root=tree.getroot()
    #
    return root

def getProbName(id):
	xml = urllib2.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem?id='+id)
	#
	tree=ET.parse(xml)
	root=tree.getroot()
	#
	return root.find(".//name").text



root = getUserData(ME)

problems = {}

for problem in root.findall(".//problem"):
	date = problem.find(".//submissiondate").text
	if(date!=None):
		problems[ date ] = problem.find(".//id").text

my_file = open('result.html','w')

my_file.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=\"utf-8\">\n\t\t<title>problems</title>\n\t</head>\n<body>")

my_file.write("<table>")

for elm in sorted(problems.items()):
	my_file.write("<tr>")
	id = elm[1]
	my_file.write("<td>")
	my_file.write("\t<a href="+"http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id="+id+"&lang=jp"+">"+id+"</a>　")
	my_file.write("</td>")
	print id
	probname = getProbName(id)
	my_file.write("<td>")
	my_file.write(probname)
	my_file.write("</td>")

	my_file.write("<td>")
	my_file.write(str(datetime.fromtimestamp( int(elm[0])/1000 )))
	my_file.write("</td>")
	my_file.write("</tr>")

my_file.write("</table>")


my_file.write("</body>\n</html>")
