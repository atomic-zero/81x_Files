#!/bin/python3

# Date: 05/19/23
# Code: Mr.p1r4t3
# Github: https://github.com/Mrp1r4t3

"""
  Install required modules:

  python3 -m pip install futures
  python3 -m pip install bs4
  python3 -m pip install requests
"""

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import os,time,json
import requests

def urlparser(url):
    if "https://" in url:
        if "youtube.com/watch?" in url:
            return True
        elif "youtu.be/" in url:
            return True
    else:
        return False

def download(youtube_url):
    global count,done
    headers = {'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Origin': 'https://yt1s.com','Referer': 'https://yt1s.com/en461/youtube-to-mp3','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Sec-GPC': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36','X-Requested-With': 'XMLHttpRequest','sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
    dat = {'q': youtube_url,'vt': 'mp3',}
    try:
        res = requests.post('https://yt1s.com/api/ajaxSearch/index', headers=headers,data=dat).text
        dt = json.loads(res.replace("'",'"'))
        mp3 = dt['links']['mp3']['mp3128']
        vid_id = dt['vid']
        out = dt['title']
        size = mp3['size']
        key = mp3['k']
        data = {'vid': vid_id,'k': key,}
        response = requests.post('https://yt1s.com/api/ajaxConvert/convert', headers=headers, data=data)
        print(response.text)
        dlink = json.loads(response.text)['dlink']
        downloadz = requests.get(dlink)
        with open(f'./{outdir}/{out}.mp3', 'wb') as file:
            file.write(downloadz.content)
            done += 1
            print(f"\033[1;92m[\033[1;93m{done}\033[1;92m] \033[1;93mSize: \033[1;91m{size} | \033[1;92mComplete => \033[1;91m{out}.mp3 \033[1;92m\033[0m")
        print(f'\033[1;92m[\033[1;91m*\033[1;92m] Downloading: [\033[1;93m{done}\033[0m/\033[1;92m{count}\033[1;92m]',end="\r")
    except KeyError:
        print(f"\033[1;91m[!] Download Failed: \033[1;93m{youtube_url}\033[0m")
def main():
    global count,done
    print("""
 \033[1;93m[ \033[1;91mYouTube to mp3 \033[1;93m]

 \033[1;91m[\033[1;92mCode\033[1;91m]\033[1;93m: \033[1;92m\033[1;97mtwp@blixors
""")
    print(" \033[1;92m[\033[1;91m1\033[1;92m] \033[1;93mDownload from file list.\n \033[1;92m[\033[1;91m2\033[1;92m] \033[1;93mDownload via single url.\n \033[1;92m[\033[1;91m0\033[1;92m] \033[1;91mExit.\n")
    try:
        sel = input("\033[1;92m[\033[1;91m?\033[1;92m] \033[1;96mSelect option: ")
        if sel in ['1','01']:
            fil = input("\033[1;92m[\033[1;91m?\033[1;92m] \033[1;96mEnter file location: ")
            if os.path.exists(fil):
                print("\033[1;92m[\033[1;94m*\033[1;92m] Threads: 25")
                print("\033[1;92m[\033[1;94m*\033[1;92m] Starting download...\n")
                with open(fil,'r') as urllist:
                    urlz = urllist.readlines()
                    count = len(urlz)
                    with ThreadPoolExecutor(max_workers=25) as downloader:
                        for us in urlz:
                            downloader.submit(download,us.strip())
                    print("\033[1;92m[\033[1;91m+\033[1;92m] Download Complete!")
            else:
                print("\033[1;91m[!] File does not exist.")
                time.sleep(3)
                os.system("clear")
                main()
        elif sel in ['2','02']:
            url = input("\033[1;92m[?] \033[1;96mEnter Youtube video url: ")
            if urlparser(url):
                print("\033[1;92m[\033[1;94m*\033[1;92m] Starting download...\n")
                count += 1
                download(url)
                print("\033[1;92m[\033[1;91m+\033[1;92m] Download Complete!")
            else:
                print(f"\033[1;91m[!] Not a valid url: {url}")
                time.sleep(3)
                os.system('clear')
                main()
        elif sel in ['0','00']:
            exit()
        else:
            print("\033[1;91m[!] Please a valid select option.")
            time.sleep(3)
            os.system('clear')
            main()
    except KeyboardInterrupt:
        exit('\n\033[1;91m[*] Exiting...')
if __name__ == "__main__":
    os.system('clear')
    outdir = "Output"
    if os.path.exists("Output") != 1:
        os.mkdir("Output")
    count, done = 0, 0
    main()
