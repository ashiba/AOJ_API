# -*- coding: utf-8 -*-

import AOJ

ME="Yazaten"

me = AOJ.User(ME)
me.getSolvedIdSet()

prob_set = set()
f = open('prob.txt','r')
for line in f:
	prob_set.add( int(line[:-1]) )

for prob in prob_set:
	if prob in me.solved_id_set:
		print( ' %04d : Solved.' % prob )
	else:
		print( ' %04d : Un Solved.' % prob )