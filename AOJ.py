from collections import defaultdict
import requests
#import xml.etree.ElementTree as ET
#import urllib.request
import json

volumes = [0,1,2,3,5,6,10,15,30,11,12,13,16,20,21,22,23,24,25,26,27,28]

findByUserIdSolutions_API_URL = ['https://judgeapi.u-aizu.ac.jp/solutions/users/','?page=0&size=5000']
findByVolume_API_URL = 'https://judgeapi.u-aizu.ac.jp/problems/volumes/'
findById_API_URL = 'https://judgeapi.u-aizu.ac.jp/users/'
class User:
	def __init__(self, user_id):
		self.user_id = user_id
		self.user_json_data		= json.loads( get_str_from_URL( findById_API_URL + self.user_id ) )
		self.solved_json_data	= json.loads( get_str_from_URL( findByUserIdSolutions_API_URL[0] + self.user_id + findByUserIdSolutions_API_URL[1] ) )
		self.user_affiliation 	= self.user_json_data['affiliation']
		self.registerdate		= self.user_json_data['registerDate']

		self.solved_id_set = set()
		self.solved_id_set_flag = False

	def get_solved_idSet(self):
		for data in self.solved_json_data:
			self.solved_id_set.add( data['problemId'] )


def get_str_from_URL(url):
	resp = requests.get( url )
	return (resp.content).decode('utf-8')


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


def get_problemID_set():
	ret = set()
	for volume in volumes:
		json_data = json.loads( get_str_from_URL( findByVolume_API_URL + str(volume) ) )
		for data in json_data['problems']:
			ret.add( data['id'] )
	return ret
