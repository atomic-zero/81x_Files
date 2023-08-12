#!/bin/python
# Coded by Mr.P1r4t3
# Date: 07/28/2022

# Facebook auto onlyme posts.

from bs4 import BeautifulSoup
import requests
cookie = "PUT YOUR ACCOUNT COOKIE HERE"
count = 0
def parse_post(url):
	global count
	headers = {
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Alt-Used': 'mbasic.facebook.com',
	    'Connection': 'keep-alive',
	    'Cookie': cookie,
	    'Upgrade-Insecure-Requests': '1',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'none',
	    'Sec-Fetch-User': '?1',
	}

	req = requests.get("https://mbasic.facebook.com"+url, headers=headers).text
	parser = BeautifulSoup(req, "html.parser")
	delp = parser.find_all("a", href=True)

	for a in delp:
		if "/privacyx/selector/?" in a['href']:
			head1 = {
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5',
               'Referer': f"https://mbasic.facebook.com{url}",
               'Alt-Used': 'mbasic.facebook.com',
               'Connection': 'keep-alive',
               'Cookie': cookie,
               'Upgrade-Insecure-Requests': '1',
               'Sec-Fetch-Dest': 'document',
               'Sec-Fetch-Mode': 'navigate',
               'Sec-Fetch-Site': 'same-origin',
               'Sec-Fetch-User': '?1',
               }
			r = requests.get("https://mbasic.facebook.com"+a["href"].split("&refid=17&_ft_")[-0]+"&priv_expand=see_all", headers=head1).text
			parser = BeautifulSoup(r, "html.parser").find_all("a", href=True)
			for x in parser:
				if 'aria-label="Only me"' in str(x):
					head2 = {
		               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
		               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		               'Accept-Language': 'en-US,en;q=0.5',
		               'Referer': f"https://mbasic.facebook.com{a['href'].split('&refid=17&_ft_')[-0]+'&priv_expand=see_all'}",
		               'Alt-Used': 'mbasic.facebook.com',
		               'Connection': 'keep-alive',
		               'Cookie': cookie,
		               'Upgrade-Insecure-Requests': '1',
		               'Sec-Fetch-Dest': 'document',
		               'Sec-Fetch-Mode': 'navigate',
		               'Sec-Fetch-Site': 'same-origin',
		               'Sec-Fetch-User': '?1',
		               }
					requests.get("https://mbasic.facebook.com"+x['href'], headers=head2)
					count += 1
					print(f" [ Success ] [ Only-me ] => {count}")
		elif "/profile/timeline/stream" in a['href']:
			if "See More Stories"in a.text:
				print(' [ Loading ]-[ New page ]')
				parse_post(a['href'])



if __name__ == '__main__':
	parse_post('/profile.php?v=timeline')
