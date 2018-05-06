#! /usr/local/bin/python3

import sys
import pprint

def usage():
	print("USAGE : python3 " + sys.argv[0] + " [FILE]")
	exit(1)

def main():
	try:
		file = open(sys.argv[1], 'r')
	except:
		usage();

	result = {}

	file.readline()
	file.readline()
	file.readline()
	
	date = file.readline()
	file.readline()
	
	data = file.readline()
	file.close()
	# print(date, data)

	beginSpecialKey = 0

	k = -1

	betweenParens = False
	for i in data:
		k+=1
		if(i == ']'):
			betweenParens = False
			try:
				result[str(data[beginSpecialKey:k])] += 1
			except:
				result[str(data[beginSpecialKey:k])] = 1
			beginSpecialKey = 0
			continue
		if(i == '['):
			betweenParens = True
			beginSpecialKey = k+1
			continue
		if(not(betweenParens)):
			try:
				result[str(i)] += 1
			except:
				result[str(i)] = 1
		

	# print(data

	date = date.replace(' ', '').replace("'", '').replace(':', '').replace('\n','')
	filename = date + ".txt"
	out = open(filename, 'w')
	for k in result:
		out.write(str(k) + " - " + str(result[k]) + '\n')
		print(str(k) + " - " + str(result[k]))
	out.close()
	print('Output saved in ' + filename)
	print('DONE')
	exit(0)

main()


