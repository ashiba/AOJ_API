# -*- coding: utf-8 -*-

# ENEMYが解いているがMEが解いていない問題を出力する

import AOJ

ME='Yazaten'
ENEMY='IS0283IR'
CHECK_DAY=20

me = AOJ.User(ME)
ene= AOJ.User(ENEMY)

me .getSolvedIdSet()
ene.getSolvedIdSet()

for probId in sorted(ene.solved_id_set):
	if probId not in me.solved_id_set:
		print( '%04d' %probId )