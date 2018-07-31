# -*- coding: utf-8 -*-
import AOJ
import sys

#user_list = ['Yazaten', 'kagasan', 'refiute', 'yurahuna', 'akahana_1', 'shichinomiya', 'kirin', 'canon4444', 'uzi7215', 'walk_to_work', 'deanagron', 'muitimon', 'mitosoup' ]
user_list = ['Yazaten', 'yurahuna', 'shichinomiya', 'hrbt', 'roto_37' ]

users = []
for user in user_list:
	tmp = AOJ.User(user)
	tmp.get_solved_idSet()
	users.append(tmp)

problemID_set = AOJ.get_problemID_set()

for user in user_list:
	sys.stdout.write( ',' + user )
print()

sys.stdout.write('# of AC')
for user in users:
	sys.stdout.write( ',' + str(len(user.solved_id_set)) )
print()


for prob_id in sorted(problemID_set):
	sys.stdout.write(prob_id)
	for user in users:
		if prob_id in user.solved_id_set:
			sys.stdout.write(', AC ')
		else:
			sys.stdout.write(',')
	print()
