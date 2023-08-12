#!/bin/python
# Code by MrP1r4t3
# python script to crack password protected zip file.

from zipfile import ZipFile
import os,sys,random,time
from datetime import datetime

def crack(passw,filen):
	global count
	try:
		with ZipFile(filen, 'r') as zipObj:
			zipObj.extractall(pwd=bytes(passw, 'utf-8'))
		print(f'\n\033[0m  [\033[0;92m Password Cracked\033[0m ] => \033[1;93m{passw} \033[0m\n')
		return True
	except Exception:
		count +=1
		if '00000' in str(count):
			print(f'\033[1;92m  [-] Attempts reached => \033[1;91m{str(count)}')
		print(f'\r\033[0m  [ \033[0;92mCracking\033[0m ]-[ \033[1;92m{str(count)} \033[0m/ \033[1;93m{to}\033[0m ]',end="",flush=True)
if __name__ == "__main__":
	count = 0
	to = ''
	try:
		f = sys.argv[1]
		pl = sys.argv[2]
		print('\033[1;91m  [-] Loading...')
		time.sleep(1)
		if os.path.exists(pl):
			if f.split('.')[-1] == 'zip':
				print()
				li = open(pl,'r').readlines()
				to += str(len(li))
				start = time.perf_counter()
				for x in li:
					if crack(x.strip(),f):
						break
				end = time.perf_counter()
				b = end - start
				ss = str(b).split('.')[-0]
				print(f"  Password cracked in {ss} seconds")
			else:
				print(' \033[1;91m [!] Cannot open file.')

		else:
			print(' \033[1;91m[!] Password list not found.')
	except IndexError:
		print(f'\n {"+-•"*10}\n Blx-Z1pcr4ck3r v1.3\n Author: 81x@7wp\n\n Usage: {sys.argv[-0]} <zipfile> <wordlist>\n {"+-•"*10}\n')
