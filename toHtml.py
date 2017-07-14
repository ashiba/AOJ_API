# -*- coding: utf-8 -*-
print "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=\"utf-8\">\n\t\t<title>problems</title>\n\t</head>\n<body>"

c=0
for line in open('res.txt','r'):
	c+=1
	print "\t<a href="+"http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id="+line+"&lang=jp"+">"+line+"</a>　"
	if c%15==0:
		print "\t<br>"

print "</body>\n</html>"
