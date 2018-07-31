# -*- coding: utf-8 -*-

import AOJ
from collections import defaultdict
from math import log10

userList=[
	"Respect2D","kioa","yokit9","ik11235","utisam","0lbBaka","nkkwe","KNKedge","slip0110",
	"komi0222","menphim","ja3rno","dispenser","arsenic28","ayihis","fukku",
	"bnsgny","CROW","is0220rk","okkyun","tmbsx","yazaten",
	"is0248vx","Nanana","satoshi31043","mots555","ixmel","pikanatsu","kerokero","futo","proru","sarada417","is0268ev","IS0283IR","moon_remon","kinono","is0266hx","Rp7rf",
	"is0384er","yebityon","shield_84"
]


def solveScore( solvedSum ):
	if solvedSum == 0:
		return -100000
	else:
		return 1.0/log10(solvedSum+1)


users_data_list = []
for user in userList:
	tmp = AOJ.User(user)
	tmp.getSolvedIdSet()
	users_data_list.append( tmp )

num_of_ac_dict = defaultdict(lambda : 0)
for data in users_data_list:
	for prob in data.solved_id_set:
		num_of_ac_dict[prob] += 1

each_score_dict = defaultdict(lambda :0)
for data in users_data_list:
	score = 0.0
	for prob in data.solved_id_set:
		score += solveScore( num_of_ac_dict[prob] )
	each_score_dict[data.id] = score

for (i, (id, score) ) in enumerate( sorted( each_score_dict.items() , key = lambda x:x[1], reverse=True) ):
	print( str(i) + ' : ' + id + '\t' + '%.3f' % (score) )
