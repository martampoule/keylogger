#! /usr/local/bin/python3

import os
import sys
import pprint
import re

folder = os.path.dirname(os.path.realpath(__file__))

t = "\t";
n = "\n";

def main():
	file = folder + "/key.txt"
	try:
		file = open(file, 'r')
		# print file
	except:
		print ("some error");



	data = file.readline()


	# copia e incolla le stringhe per rilevare eventuali altri tasti non presenti nella lista
	# -------------
	match_unknown = "[unknown]"
	unknown = len(data.split(match_unknown)) - 1

	match_tab = "[tab]"
	tab = len(data.split(match_tab)) - 1
	
	match_caps = "[caps]"
	caps = len(data.split(match_caps)) - 1

	match_left_shift = "[left-shift]"
	left_shift  = len(data.split(match_left_shift)) - 1

	match_right_shift = "[right-shift]"
	right_shift  = len(data.split(match_right_shift)) - 1
	
	match_fn = "[fn]"
	fn  = len(data.split(match_fn)) - 1

	match_left_ctrl = "[left_ctrl]"
	left_ctrl  = len(data.split(match_left_ctrl)) - 1

	match_right_ctrl = "[right_ctrl]"
	right_ctrl  = len(data.split(match_right_ctrl)) - 1

	match_left_option = "[left-option]"
	left_option = len(data.split(match_left_option)) - 1
	
	match_right_option = "[right-option]"
	right_option = len(data.split(match_right_option)) - 1

	match_left_cmd = "[left-cmd]"
	left_cmd = len(data.split(match_left_cmd)) - 1

	match_right_cmd = "[right-cmd]"
	right_cmd  = len(data.split(match_right_cmd)) - 1

	match_del = "[del]"
	_del = len(data.split(match_del)) - 1

	match_return = "[return]"
	_return = len(data.split(match_return)) - 1

	match_up = "[up]"
	up = len(data.split(match_up)) - 1

	match_down = "[down]"
	down = len(data.split(match_down)) - 1

	match_left = "[left]"
	left = len(data.split(match_left)) - 1

	match_right = "[right]"
	right = len(data.split(match_right)) - 1




	# inserisci su replace_list eventuali altri tasti non presenti nella lista
	# -------------
	replace_list = [match_unknown,match_fn,match_right_option,match_right_ctrl,match_del,match_right,match_return,match_left,match_right_cmd,match_caps,match_left_ctrl,match_right_shift,match_right_shift,match_left_cmd,match_left_shift,match_left_option,match_tab,match_down,];
	txt = re.sub("|".join(map(re.escape, replace_list)), "", data)

        
##	filename = date.replace(' ', '').replace("'", '').replace(':', '').replace('\n','') + ".txt"
##	print (filename)
	filename = "out.txt"
	out = open(filename, 'w')


	# inserisci eventuali altri tasti non presenti nella lista
	# -------------
	out.write(match_unknown + t + str(unknown) + n)
	out.write(match_tab + t + str(tab) + n)
	out.write(match_caps + t + str(caps) + n)
	out.write(match_left_shift + t + str(left_shift) + n)
	out.write(match_right_shift + t + str(right_shift) + n)
	out.write(match_fn + t + str(fn) + n)
	out.write(match_left_ctrl + t + str(left_ctrl) + n)
	out.write(match_right_ctrl + t + str(right_ctrl) + n)
	out.write(match_left_option + t + str(left_option) + n)
	out.write(match_right_option + t + str(right_option) + n)
	out.write(match_right_cmd + t + str(right_cmd) + n)
	out.write(match_left_cmd + t + str(left_cmd) + n)
	out.write(match_del + t + str(_del) + n)
	out.write(match_return + t + str(_return) + n)
	out.write(match_up + t + str(up) + n)
	out.write(match_down + t + str(down) + n)
	out.write(match_left + t + str(left) + n)
	out.write(match_right + t + str(right) + n)


	# inserisci qui di seguito tutti i tasti che vuoi rilevare
	# -------------
	key = "abcdefghijklmnopqrstuvwxyz1234567890/\.,;`'=-][";
	for a in key:
	    out.write(a + t + str(txt.count(a)) + n)

	out.close()
	print("done")

main()


""""

apri il terminale e incolla la seguente stringa 

python keyloggerParser.py



"""

