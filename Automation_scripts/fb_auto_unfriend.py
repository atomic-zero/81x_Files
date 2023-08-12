#!/bin/python
# 08/12/2023

# Code by MrP1r4t3
# python script to unfriend fast in facebook.

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests

unfriended = 0
total = 0
friends = 0
user_cookie = "PUT YOUR FACEBOOK COOKIE HERE"

dumped = {}

def unfriend(uid,name):
	global unfriended
	if uid.isdigit():
		headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','accept-language': 'en-US,en;q=0.5','cache-control': 'max-age=0','cookie': user_cookie,'referer': f'https://mbasic.facebook.com/profile.php?id={uid}','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','sec-gpc': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.30 Mobile Safari/537.36'}
		params = {'friend_id': uid,'unref': 'profile_gear',}
		req = requests.session()
		response = req.get('https://mbasic.facebook.com/removefriend.php', params=params, headers=headers)
		parser = BeautifulSoup(response.text,'html.parser')
		form = parser.find('form',method='post')
		data = {'fb_dtsg':form.find('input',{'name':'fb_dtsg'}).get('value'),'jazoest': form.find('input',{'name':'jazoest'}).get('value'),'confirm':'Confirm'}
		headers.update({'content-type': 'application/x-www-form-urlencoded','origin': 'https://mbasic.facebook.com','referer': response.url,})
		req.post('https://mbasic.facebook.com'+form.get('action'),headers=headers,data=data)
		unfriended+=1
		print(f'\x1b[0m[\x1b[0;32m{uid}\x1b[0m] {name} \x1b[0;31mUnfriended.\x1b[0m')
		print(f'\r\x1b[0m[\x1b[0;32m*\x1b[0m] Unfriending: \x1b[0;31m{unfriended}\x1b[0m/\x1b[0;32m{total}',end='')
	else:
		headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','accept-language': 'en-US,en;q=0.5','cookie': user_cookie,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','sec-gpc': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.30 Mobile Safari/537.36',}
		user_id = [ x for x in BeautifulSoup(requests.get('https://mbasic.facebook.com/'+uid, headers=headers).text,'html.parser').find_all('a',href=True) if '/privacy/touch/block/confirm/'in str(x)][0].get('href').replace('/privacy/touch/block/confirm/?bid=','').split('&')[-0]
		unfriend(user_id,name)

def dump_friendlist(url=None):
	global total,friends
	if url == None:
		url = 'https://mbasic.facebook.com/profile.php?v=friends'
	headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','accept-language': 'en-US,en;q=0.5','cache-control': 'max-age=0','cookie': user_cookie,'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','sec-gpc': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.30 Mobile Safari/537.36',}
	req = requests.session()
	response = req.get(url,headers=headers).text
	parser = BeautifulSoup(response,'html.parser')
	try:
		if total == 0:
			total = int(''.join([x for x in [*parser.find('h3').text] if x.isdigit()]))
	except:
		print('[!] Unable to find friends list total.')
		exit()
	table = [x for x in parser.find_all('tr') if 'profile picture' in str(x)]
	for x in table:
		data = x.find('a')
		name = data.text
		if 'profile.php?id=' in str(data.get('href')):
			user_id = data.get('href').replace('/profile.php?id=','').split('&')[-0]
		else:
			user_id = data.get('href').replace('/','').split('?')[-0]
		if "mbasic" not in str(user_id):
			dumped.update({user_id:name})
			friends += 1
	print(f'\x1b[0m[\x1b[0;32m*\x1b[0m] Dumping friends: \x1b[0;31m{len(dumped)}\x1b[0m/\x1b[0;32m{total}', end='\r')
	try:
		cursor = 'https://mbasic.facebook.com'+parser.find('div',id='m_more_friends').find('a',href=True).get('href')
		dump_friendlist(cursor)
	except AttributeError:
		pass

if __name__ == '__main__':
	dump_friendlist()
	print('\x1b[0m[\x1b[0;32m*\x1b[0m] Unfriending Friends...')
	with ThreadPoolExecutor(max_workers=10) as thread:
		for x in dumped.keys():
			thread.submit(unfriend, x.strip(),dumped.get(x).strip())
	print('\x1b[0m[\x1b[0;32m*\x1b[0m] Done, The remaining is someone that u followed.')
