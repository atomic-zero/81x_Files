#!/bin/python3
# Code by Mr.P1r4t3
# Facebook simple chatbot written in python
# Note: Outdated version
# Purpose: To have anyone an idea for making fb chatbots.



import requests
import time
import yaml
import random
import os
import itertools
from bs4 import BeautifulSoup
import threading

user_id = "FACEBOOK ACCOUNT ID"

done = False
myname = ""
bot_name = ""
bot_cookie = ""
quotes = ["Never ignore a person who loves you, care for you, and misses you, because one day, you might wake up and realize, you lost the moon while counting the stars.","The purpose of our lives is to be happy.","Life is what happens when you're busy making other plans.","You only live once, but if you do it right, once is enough.","Many of life’s failures are people who did not realize how close they were to success when they gave up.","Money and success don’t change people; they merely amplify what is already there.","Not how long, but how well you have lived is the main thing.","In order to write about life first you must live it.","There is never a time or place for true love. It happens accidentally, in a heartbeat, in a single flashing, throbbing moment.","Love is that condition in which the happiness of another person is essential to your own.","He is not a lover who does not love forever.","Love does not begin and end the way we seem to think it does. Love is a battle, love is a war; love is a growing up.","We can only learn to love by loving."]
hugot_lines = ["Masakit ang maiwan, pero mas masakit ang manatili sa isang relasyong alam mong ikaw na lang ang nagmamahal.", ") Kung  respeto ang hinahanap mo, unahin mo munang respetuhin sarili mo.","Minsan nakakatamad na din magseryoso. Lalo na’t parati ka nalang niloloko.","Mahal mo kasi maputi? It’s not love, it’s Dove!.","Wag kang magpakatanga sa taong binabalewala ka.","Pwede ba tayong magkunwaring mahal natin ang isat-isa?? Tapos totohanin na lang natin pag-naniwala na sila.","Hindi ka bibigyan ng “pagsubok ni lord” kung alam niyang hindi mo kaya."," Bakit ang hirap mag move on sa taong minahal mo ng sobra… peru kahit minsan, hindi mo man lang naramdamang minahal ka."," Ang mag syota daw ay parang presyo ng bagong model na cellphone. Sa una nagmamahalan tapos di magtatagal magmumurahan!","Kapag nakikita kitang malungkot at nag iisa, gusto kitang lapitan at damayan, yayakapin ng mahigpit at sabhing nandito lang ako para sayo. Kaso di ko magawa baka kasi sabihin mo… sorry hindi ikaw ang kailangan ko."," Sa panahon ngayon, bihira na yung babaeng kinakasal muna bago mabuntis."," Hindi ko naman hinihiling na ako ang unahin mo. Ayoko lang maramdaman na parang wala lang ako sayo.","Kung tinanong ka ng manliligaw mo kung chocolates o flowers… be practical! Bigas men bigas!"]

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def bot_message(url, command):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://mbasic.facebook.com/messages/?folder=unread',
        'Alt-Used': 'mbasic.facebook.com',
        'Connection': 'keep-alive',
        'Cookie': bot_cookie,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    req = requests.Session()
    parse = req.get(f'https://mbasic.facebook.com{url}', headers=headers).text
    pars = BeautifulSoup(parse, "lxml")
    fb_dtsg = pars.find('input', {'name': 'fb_dtsg'})['value']
    jazoest = pars.find('input', {'name': 'jazoest'})['value']
    wwwupp = pars.find('input', {'name': 'wwwupp'})['value']
    cver = pars.find('input', {'name': 'cver'})['value']
    tids = pars.find('input', {'name': 'tids'})['value']
    csid = pars.find('input', {'name': 'csid'})['value']

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': f'https://mbasic.facebook.com{url}',
        'Origin': 'https://mbasic.facebook.com',
        'Alt-Used': 'mbasic.facebook.com',
        'Connection': 'keep-alive',
        'Cookie': bot_cookie,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    params = {
        'icm': '1',
        'refid': '12',
    }
    ids = url.split(tids.split(":")[-1])
    data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'body': command,
        'send': 'Send',
        'tids': tids,
        'wwwupp': wwwupp,
        f'ids[{ids}]': ids,
        'referrer': '',
        'ctype': '',
        'cver': cver,
        'csid': csid,
    }

    response = requests.post('https://mbasic.facebook.com/messages/send/', params=params, headers=headers, data=data)

def dictionary(word):

    #can’t be found in the dictionary.

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': f'https://www.merriam-webster.com/dictionary/{word}',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    results = requests.get(f'https://www.merriam-webster.com/dictionary/{word}',headers=headers).text
    if "can’t be found in the dictionary." in results:
        return f"{bot_name} No search result for {word}"
    elif "The word you've entered isn't in the dictionary. Click on a spelling suggestion below or try again using the search bar above." in results:
        return f"{bot_name} No search result for {word}"
    else:
        parser = BeautifulSoup(results, "lxml").find("div", id="dictionary-entry-1")
        import re
        sr = re.sub(r"\s+", " ", parser.text, flags=re.UNICODE)
        return sr

def send_message(name, url):
#    print("runing...")
    my_message = f"Hi there {name} my name is {bot_name}🥰😗\nI am a B0t created by Mrp1r4t3.😗🥳😎\n {myname} is kinda busy right now you can leave a message for him💖, but make sure you start it with '{bot_name}' 😘 so \nI don't reply again with this message.\nQuote for you:   {random.choice(quotes)}   \nAvailable commands:\nquotes\nhugot_line\ninfo\nplay (not available right now.)\nreact (not available right now)\ncomment (not available right now)\n{bot_name} replied at {current_time}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://mbasic.facebook.com/messages/?folder=unread',
        'Alt-Used': 'mbasic.facebook.com',
        'Connection': 'keep-alive',
        'Cookie': bot_cookie,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    req = requests.Session()
    parse = req.get(f'https://mbasic.facebook.com{url}', headers=headers).text
    pars = BeautifulSoup(parse, "lxml")
    fb_dtsg = pars.find('input', {'name': 'fb_dtsg'})['value']
    jazoest = pars.find('input', {'name': 'jazoest'})['value']
    wwwupp = pars.find('input', {'name': 'wwwupp'})['value']
    cver = pars.find('input', {'name': 'cver'})['value']
    tids = pars.find('input', {'name': 'tids'})['value']
    csid = pars.find('input', {'name': 'csid'})['value']

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': f'https://mbasic.facebook.com{url}',
        'Origin': 'https://mbasic.facebook.com',
        'Alt-Used': 'mbasic.facebook.com',
        'Connection': 'keep-alive',
        'Cookie': bot_cookie,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    params = {
        'icm': '1',
        'refid': '12',
    }
    ids = url.split(tids.split(":")[-1])
    data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'body': my_message,
        'send': 'Send',
        'tids': tids,
        'wwwupp': wwwupp,
        f'ids[{ids}]': ids,
        'referrer': '',
        'ctype': '',
        'cver': cver,
        'csid': csid,
    }

    response = requests.post('https://mbasic.facebook.com/messages/send/', params=params, headers=headers, data=data)


def loading():
    try:
        loading1 = ["[\033[1;91m-\033[1;92m] Bot is running.  ","[\033[1;91m/\033[1;92m] Bot is running\033[1;92m.. ","[\033[1;91m\\\033[1;92m] Bot is running\033[1;92m...","[\033[1;91m-\033[1;92m] Bot is running   "]
        for i in itertools.cycle(loading1):
            if done == True:
                break
            print(f'\r\033[1;92m {i}\033[0m',end="")
            time.sleep(0.3)
            continue
    except KeyboardInterrupt:
        exit()


def read_messages():
    while True:
        headers = {
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Alt-Used': 'mbasic.facebook.com',
            'Connection': 'keep-alive',
            'Cookie': bot_cookie,
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
        }
        res = requests.get('https://mbasic.facebook.com/messages/?folder=unread', headers=headers).text
        parser = BeautifulSoup(res, "lxml")
        trs = parser.find_all("tr")
        for tr in trs:
            abbr = tr.find_all("abbr")
            for x in abbr:
               if "Just now" in x.text:
                    a = tr.find("a", href=True)
                    if f"{user_id}%3A" in a["href"]:
                        if f"{bot_name}" in tr.find('span').text:
                            pass
                        elif "ۦۦ ۦۦ" in a.text:
                            pass
                        elif "quote" in tr.find('span').text:
                            bot_message(a['href'].split("&")[-0],bot_name+'\n'+random.choice(quotes))
                        elif "hugot_line" in tr.find('span').text:
                            bot_message(a['href'].split("&")[-0],bot_name+"\n"+random.choice(hugot_lines))
                        elif "dictionary" in tr.find('span').text:
                            bot_message(a['href'].split("&")[-0], bot_name+"\n"+dictionary(tr.find('span').text.split(" ")[-1]))
                        else:
                            print("\r                           ")
                            print(f" \033[1;91m{a.text} \033[1;92mSent you a message at \033[1;93m{current_time}")
                            print("\r","\033[1;92m-"*50)
                            print(f" \033[1;92mMessage \033[1;93m=> \033[1;96m{tr.find('span').text} \n")
                            send_message(a.text.split(" ")[-0], a['href'].split("&")[-0])
                            print("\r                           ")

               elif "minutes ago" in x.text:
                    a = tr.find("a", href=True)
                    if f"{user_id}%3A" in a["href"]:
                        if f"{bot_name}" in tr.find('span').text:
                            pass
                        elif "ۦۦ ۦۦ" in a.text:
                            pass
                        elif "quote" in tr.find('span').text:
                            bot_message(a['href'].split("&")[-0],bot_name+'\n'+random.choice(quotes))
                        elif "hugot_line" in tr.find('span').text:
                            bot_message(a['href'].split("&")[-0],bot_name+"\n"+random.choice(hugot_lines))
                        elif "dictionary" in tr.find('span').text:
                            bot_message(a['href'].split("&")[-0], bot_name+"\n"+dictionary(tr.find('span').text.split(" ")[-1]))
                        else:
                            print("\r                           ")
                            print(f" \033[1;91m{a.text} \033[1;92mSent you a message at \033[1;93m{current_time}")
                            print(f" \033[1;92mMessage \033[1;93m=> \033[1;96m{tr.find('span').text} \n")
                            send_message(a.text.split(" ")[-0], a['href'].split("&")[-0])
                            print("\r                           ")

def chk(cookie):
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

    profile = BeautifulSoup(requests.get('https://mbasic.facebook.com/profile.php',headers=headers).text, "lxml").title.text
    if profile in ["Page Not Found", "Content Not Found"]:
        print("Cookie is expired.")
        exit()
    elif "log" in profile:
        print("Cookie is expired.")
        exit()
    else:
        with open("config.yml", "a") as conf:
            name = profile.split(" ")[-0]
            conf.write(f"myname: {name}\n")
            conf.write(f"bot_cookie: {cookie}\n")
            conf.close()
        print("cookie is ok.")

def botsetup():
    while True:
        try:
            botn = input("Enter bot name > ")
            if botn in ["", " "]:
                print("enter a valid bot name.")
            else:
                with open("config.yml", "a") as conf:
                    conf.write("bot_name: "+botn)
                    conf.close()
                print("Setup complete!\nPlease run again the program.")
                exit()
        except KeyboardInterrupt:
            print("\nAborting...")
            os.system("rm config.yml")


def setup():
    encookie = input("Enter cookie > ")
    if "c_user" in encookie:
        print("checking cookie...")
        chk(encookie)
        botsetup()
    else:
        print("Cookie is invalid.")
        exit()

def run():
    print(" \033[1;91m[*] \033[1;92mRequest timeout: 5 seconds.")
    print("","="*50)
    print()
    try:
        time.sleep(2)
 #      print("hsbbs")
        read_messages()
    except KeyboardInterrupt:
        print("\n [*] Shutting down...")
        exit()



def main():
    if os.path.exists("config.yml"):
        global myname
        global bot_name
        global bot_cookie
        with open("config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
            myname += cfg['myname']
            bot_cookie += cfg['bot_cookie']
            bot_name += cfg["bot_name"]
            ymlfile.close()
        run()
    else:
        print("starting setup....")
        setup()


if __name__ == '__main__':
    main()

