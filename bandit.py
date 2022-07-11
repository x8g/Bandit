from distutils.util import execute
from discord_webhook import DiscordWebhook
import os, threading, requests
from pystyle import *


url = 'webhook'
# ----
os.system('cls & mode 83, 22')
#
os.system('title Bandit Username Checker')
with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    sid = input(Colorate.Horizontal(Colors.blue_to_purple, 'Sid?: '))
    threads = input(Colorate.Horizontal(Colors.blue_to_purple, 'Threads? (5 or less): '))
# ----
def check():
    while True:
     for username in usernames:
      checkurl = (f"https://www.tiktok.com/api/user/detail/?uniqueId={username}")
      checkhed = {
          "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
          "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ccept-encoding: gzip, deflate, br",
          "scheme": "https",
          "cookie": f"sessionid={sid}" }
      checkreq = requests.get(checkurl, headers=checkhed)
      print(checkreq.text)
      if '"statusCode":10202' in (checkreq.text):
            print(Colorate.Horizontal(Colors.blue_to_purple, 'Webhook Sent | Avail User! | ' + username))
            webhook = DiscordWebhook(url=url, content=f'``{username}`` is available!')
            webhook = execute()
            with open('available.txt', "a") as x:
             x.write(f"{username}\n")
      if '"statusCode":0' in (checkreq.text):
            print(Colorate.Horizontal(Colors.red_to_white, "Taken User! | " + username))
      if '"statusCode":10221' in (checkreq.text):
            print(Colorate.Horizontal(Colors.red_to_white, "Banned User! | " + username))    
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=check).start()
