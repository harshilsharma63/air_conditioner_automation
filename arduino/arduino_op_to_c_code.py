#!/usr/bin/python3

import sys;

file_path = sys.argv[1]

ardino_code = ""

for line in open(file_path):
	data = [x.strip() for x in line.split(',')]
	print("delayMicroseconds("+ data[0] +");")
	print("pulseIR("+ data[1] +");")
