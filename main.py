from os import system
import requests , uuid , time 
import os
import time
from colorama import Fore, Back, Style
import sys
import json

if sys.version_info[0] < 3:
	pyversion = python_version()
	print("Alert! Your python version is %s. Use python version 3> to run this code" %(pyversion))
	exit(1)

req = requests.session()
uid = uuid.uuid4()
system("title " + "t.me/undecryptable")
os.system('cls||clear')
print(Back.BLACK + Fore.MAGENTA + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')
print('')
print(Fore.CYAN + '          Critical Ops Player Search by yin/who?')
print('')
print('')
user = input(Back.BLACK + Fore.WHITE + "Enter Username: ")

data = {"usernames":[user]}
#if you get error you need to update authorization cookie "bearer etc"
headers = {
    'accept': '*/*',
    'content-type': 'application/json',
    'x-apiversion': '1.28.0.f1605',
    'authorization': 'Bearer NzEwNzQ0NzQzOjM4Njk4ODA3MTI3MDBlZjQzNzY5MzRkYTc5MWE2MTNmOjY4MTcyNzI5MTpiNGM0NjI3YjIyNjUwODk1OTY2MmUzNDcwNzY1MmQyYTpjY3pIY3Iyc2lFRlRCQml3TitXUlpvQTd5ZWJ5ei93R0xFTjJIM21rQUIzTjlvUFEzRHk1bkswa2Z0OE4rcExRK1BUdCtCZzJpajNwbkE2QVF3cWN0dz09',
    'content-length': '21',
    'x-unity-version': '2020.3.19f1',
    'accept-language': 'en-ca',
    'user-agent': 'CriticalOps/1765 CFNetwork/1128.0.1 Darwin/19.6.0',
    'accept-encoding': 'gzip, deflate, br',
    'Host': '1-28-0.prod.copsapi.criticalforce.fi'}
url = "https://1-28-0.prod.copsapi.criticalforce.fi/api/user/find/usernames/"
res = requests.post(url,json=data,headers=headers)
#note from Timer1337: "play stupid games win stupid prizes :)"
os.system('cls||clear')
system("title t.me/undecryptable")
print(Back.BLACK + Fore.MAGENTA + '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"')
print('')
print(Fore.CYAN + f'         "{user}" Player Info')
print('')
print('')
#by yin/who?/timer/kevin
json_object = json.dumps(res.json(), indent = 4)
f = open("playerinfo.json", "w")
f.write(json_object)
f.close()
print(json_object)
print('')
print('')
print("Saved in playerinfo.json")
print('')
