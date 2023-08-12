# Date: Sun Apr 23 03:12:38 AM CST 2023
# A simple SQLi Vulnerability checker...
# Coded: MrP1r4t3

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import time,os


"""
Install requirements:

- For requesting to server
pip install requests

- For parsing Urls
pip install bs4

- For multi thread
pip install futures
"""

# Number of threads
thread_number = 30
# Vuln verifyer
custom = ["'",'"']

def get_base_url(url):
	# Parse Base URL
	l = 0
	i = 0
	d = []
	for x in url:
		d.append(x)
		if '/' in x:
			l +=1
		if l == 3:
			break
	for xd in url:
		if '/' == xd:
			i += 1
	if i == 3:
		return ''.join(d)
	elif i == 2:
		return url+'/'
	else:
		return 'ERROR'

def request_url(url):
	data = []
	urlz = []
	base_url = get_base_url(url)
	print(f" \033[1;93m[*] Connecting --> {url}")
	# List error to verify if vuln
	erlist = [
    "<b>Warning</b>:  SQLite3",
    "unrecognized token:",
    "Unable to prepare statement:",
    "You have an error in your SQL",
    "MySQL server version for the right syntax",
    "supplied argument is not a valid MySQL result resource",
    "ERROR:  syntax error"
    ]
	if multi != 1:
		vuln_found = True
	if base_url == "ERROR":
		print(f"\033[1;91m [!] ERROR while parsing base url: {url}")
	else:
		# Headers to bypass some restrictions
		headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'en-US,en;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',}
		req = requests.session()
		re = req.get(url,headers=headers)
		parser = BeautifulSoup(re.text, 'html.parser')
		try:
			# Extract all links on <a href=*>
			for x in parser.find_all('a', href=True):
				if '=' in x['href']:
					int(x['href'].split('=')[-1])
					# Check if http | https is present
					if 'http' not in x['href'] or 'https' not in x['href']:
						if x['href'].replace('/','').split('?')[-0] not in data:
							# Get only links with params
							data.append(x['href'].replace('/','').split('?')[-0]);urlz.append(x['href'])
					else:
						if '=' in x['href'].split('?')[-1]:
							int(x['href'].split('?')[-1].split('=')[-1])
							if x['href'].split('?')[-0] not in data:
								# same here
								data.append(x['href'].split('?')[-0]);urlz.append(x['href'])

		except:
			pass
		for targp in urlz:
			if "https" in targp or "http" in targp:
				pass
			else:
				# Check if vulnerable
				for quick in custom:
					x = req.get(base_url+targp+quick,headers=headers)
					for sd in erlist:
						if sd in x.text:
							if multi != 1:
								vuln_found = False
							print(f"\033[1;92m [+] Vuln: {x.url}")
	if multi != 1:
		if vuln_found:
			print(" [!] No SQLi vuln params found...")


if __name__ == "__main__":
	multi = 0
	banner = """

		-=[ Coded: 7wp@81x ]=-

 A simple multi threaded Sqli checker.

 1. Single target url
 2. multiple urls (file list)
 0. exit
	"""
	print(banner)
	while True:
		try:
			inp = int(input(" --> "))
			if inp == 1:
				targu = input(" Enter Target url -> ")
				if "http://" in targu or "https://" in targu:
					request_url(targu)
					exit()
				else:
					print(" [!] Enter a valid url.")
					time.sleep(3)
					os.system('clear')
					print(banner)
			elif inp == 2:
				multi += 1 
				targu = input(" Enter file list -> ")
				if os.path.exists(targu):
					with open(targu,'r') as flist:
						# Establish multiple connection
						with ThreadPoolExecutor(max_workers=thread_number) as exb:
							for fileu in flist.readlines():
								if "http://" in fileu or "https://" in fileu:
									exb.submit(request_url, fileu.strip())
					print("\n\033[1;92m [+] Done")
					exit()
				else:
					print("\033[1;91m [!] File not exist!")
					time.sleep(3)
					os.system('clear')
					print(banner)
			elif 0:
				exit()
			else:
				print("\033[1;91m [!] Select only: 1, 2, 0")
				time.sleep(3)
				os.system('clear')
				print(banner)
		except ValueError:
			print("\033[1;91m [!] Select only: 1, 2, 0")
		except KeyboardInterrupt:
			print("\033[1;91m Bye bye!")
			exit()
