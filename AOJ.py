from collections import defaultdict
import xml.etree.ElementTree as ET
import urllib.request

class User:
	def __init__(self, user_id):
		self.user_id = user_id
		self.root = self.get_user_root()

		self.solved_id_set = set()
		_self.solved_id_set_flag = False


	def _get_user_root(self):
		http_resp = urllib.request.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id='+self.user_id)
		tree = ET.parse( http_resp )
		root = tree.getroot()
		return root


	def get_solved_idSet(self):
		for problemID in self.root.findall(".//problem/id"):
			self.solved_id_set.add( int(problemID.text) );



def get_under_meList(rankList):
	retList=[]
	isFoundMe=0
	for user_id in rankList:
		if isFoundMe==1 :
			retList.append(id)
		#
		if user_id[0]==ME :
			isFoundMe=1
	#
	return retList


def get_prob_name(prob_id):
	http_resp = urllib.request.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem?id='+prob_id)
	root=getRoot( http_resp )
	#
	return root.find(".//name").text


