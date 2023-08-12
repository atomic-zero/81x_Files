#!usr/bin/python
# Coded by mrp1r4t3
# Hide all post in your timeline

from bs4 import BeautifulSoup
import random
import time
import requests

cookie = "PUT YOUR FB ACCOUNT COOKIE HERE"
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
    parser = BeautifulSoup(req, "lxml")
    delp = parser.find_all("a", href=True)
    for a in delp:
        if "direct_actions/?context_str" in a['href']:
            head1 = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': 'https://mbasic.facebook.com/profile.php?v=timeline',
                'Alt-Used': 'mbasic.facebook.com',
                'Connection': 'keep-alive',
                'Cookie': cookie,
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
            req = requests.Session()
            parser = BeautifulSoup(req.get("https://mbasic.facebook.com"+a['href'],headers=head1).text, "lxml")
            jazoest = parser.find('input', {'name': 'jazoest'})['value']
            fb_dtsg = parser.find('input', {'name': 'fb_dtsg'})['value']
            action = parser.find("form", method="post")['action']
            re = a['href']

            head2 = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': f'https://mbasic.facebook.com{re}',
                'Origin': 'https://mbasic.facebook.com',
                'Alt-Used': 'mbasic.facebook.com',
                'Connection': 'keep-alive',
                'Cookie': cookie,
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
            data = {
                'fb_dtsg': fb_dtsg,
                'jazoest': jazoest,
                'action_key': 'HIDE_FROM_TIMELINE',
                'submit': 'Submit',
            }

            response = req.post(f'https://mbasic.facebook.com{action}', headers=head2, data=data)
            count += 1
            print(f"\r Hidden posts => {count}",end='')
        elif "/profile/timeline/stream" in a['href']:
            if "See More Stories"in a.text:
                parse_post(a['href'])




if __name__ == "__main__":
    parse_post('/profile.php?v=timeline')
