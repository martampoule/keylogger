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

	match_del = "[del]"
	_del = len(data.split(match_del)) - 1

	match_return = "[return]"
	_return = len(data.split(match_return)) - 1

	match_left_cmd = "[left_cmd]"
	left_cmd  = len(data.split(match_left_cmd)) - 1

	match_right_cmd = "[right-cmd]"
	right_cmd  = len(data.split(match_right_cmd)) - 1

	match_left_shift = "[left-shift]"
	left_shift  = len(data.split(match_left_shift)) - 1

	match_left_option = "[left-option]"
	left_option = len(data.split(match_left_option)) - 1

	match_tab = "[tab]"
	tab = len(data.split(match_tab)) - 1

	match_up = "[up]"
	up = len(data.split(match_up)) - 1

	match_down = "[down]"
	down = len(data.split(match_down)) - 1


	# inserisci su replace_list eventuali altri tasti non presenti nella lista
	# -------------
	replace_list = [match_unknown,match_del,match_return,match_right_cmd,match_left_cmd,match_left_shift,match_left_option,match_tab,match_down];
	txt = re.sub("|".join(map(re.escape, replace_list)), "", data)

        
##	filename = date.replace(' ', '').replace("'", '').replace(':', '').replace('\n','') + ".txt"
##	print (filename)
	filename = "out.txt"
	out = open(filename, 'w')


	# inserisci eventuali altri tasti non presenti nella lista
	# -------------
	out.write(match_unknown + t + str(unknown) + n)
	out.write(match_del + t + str(_del) + n)
	out.write(match_return + t + str(_return) + n)
	out.write(match_right_cmd + t + str(right_cmd) + n)
	out.write(match_left_cmd + t + str(left_cmd) + n)
	out.write(match_left_shift + t + str(left_shift) + n)
	out.write(match_left_option + t + str(left_option) + n)
	out.write(match_tab + t + str(tab) + n)
	out.write(match_up + t + str(up) + n)
	out.write(match_down + t + str(down) + n)


	# inserisci qui di seguito tutti i tasti che vuoi rilevare
	# -------------
	key = "abcdefghijklmnopqrstuvwxyz";
	for a in key:
	    out.write(a + t + str(txt.count(a)) + n)

	out.close()
	print("done")

main()


""""

apri il terminale e incolla la seguente stringa 

python keyloggerParser.py



"""

