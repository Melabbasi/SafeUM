import os
import sys
import time
import random
from gzip import decompress
from concurrent.futures import ThreadPoolExecutor
from json import dumps
from random import choice, choices

try:
    from websocket import create_connection
except ModuleNotFoundError:
    os.system('pip install websocket-client')
    from websocket import create_connection

try:
    from user_agent import generate_user_agent
except ModuleNotFoundError:
    os.system('pip install user_agent')

try:    
    import pyfiglet
except ModuleNotFoundError:
    os.system('pip install pyfiglet')

try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')

from ssl import CERT_NONE

# ANSI color codes for styling
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[1;97m"
y = '\033[1;35m'

failed = 0
success = 0
retry = 0
accounts = []

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0625)  # Adjusted delay for smoother output

def work():
    global failed, success, retry
    username = choice('qwertyuiooasdfghjklzxcvpbnm') + ''.join(choices('qwertyuioasdfghjklzxcvbnpm1234567890', k=16))
    try:
        con = create_connection(
            "wss://195.13.182.213/Auth",
            header={"app": "com.safeum.android", "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195"},
            sslopt={"cert_reqs": CERT_NONE}
        )
        con.send(dumps({
            "action": "Register",
            "subaction": "Desktop",
            "locale": "ar_EG",
            "gmt": "+03",
            "password": {
                "m1x": "674aa02c68df3f5c3fa11c7904b897532a17e50757f5a4252338aa00b49b2932",
                "m1y": "9333b68c189bffa2935cdada6043ed9335c07ee9261535d8ddb4d7c0eb38c13c",
                "m2": "9ddf1837873f902e9988d41f95f260303718bc8e3db872eebef871044a082975",
                "iv": "87fa6e2284c7e219026975f72a5d423f",
                "message": "d94df8c6593e7984970a41adf9dabd695265fa7363403717c7d7255060aa7a092997fd9c34ee6f055529eca9a7275a38bb0073c3209233c94b7f2c9b7a6971d5924317b481075c1ce1dde807ea5ea1d8"
            },
            "magicword": {
                "m1x": "fa9dc82e219d8580e79acdc107f2593e73990034e386da7e53ef0552e42a1395",
                "m1y": "25d2d66f684bc7a661cc2085ade22c41051b654f46ee2865bc171db38307c151",
                "m2": "e85b5efc89564e1572861db4853af60cbc3b92e5a093f5735605ebdd8e1ddd8a",
                "iv": "f7c847f7152dacf890a18f34bdfc07e3",
                "message": "4f36925ed7fca213fb0f6b37ba906808"
            },
            "magicwordhint": "0000",
            "login": str(username),
            "devicename": "INFINIX Infinix X678B",
            "softwareversion": "1.1.0.2300",
            "nickname": "skksoskzhjdjridbn",
            "os": "AND",
            "deviceuid": "4b81ce4e8c8208f4",
            "devicepushuid": "*fZigg-TFSgij1Gr09Zduj3:APA91bH3N3I0dXrTR8lQ5SCYdbKLSDq6B-N5c3GF_ZkF5kRFQeHEc08hyAbq7Mn25v1d0jpjSxZopdyuIGFfTyq0jgpE7G8GNV-jI8j_ouOgysLe-DYzP7q9czJlkmA6UJn6QDDdxMzw",
            "osversion": "and_13.0.0",
            "id": "543208426"
        }))
        
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            accounts.append(f'{username}')
            with open('SafeUM_abbasi.txt', 'a') as f:
                f.write(f'{username} : aaaa | @mohamed__elabbasi on Instagram\n')
        else:
            failed += 1
    except Exception:
        retry += 1

start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print(X + "_" * 67)
    print(C + '                     For more tools ->')
    print(y + '                         @mohamed__elabbasi on instagram               ')
    print(X + "_" * 67)
    print(F + '')
    print(f'\n\n\Accounts number : {success}\n\n\n{Z}Number of clicks : {failed}\n\n\n{X}Number of tries : {retry}{F}\n\n\n')

    if success >= 2990:
        # Implement your shutdown function here
        print(F + "Accounts successfully generated!")
        
    if success > 0:
        z = "\n".join(accounts)
        print(F + "The accounts have been created by the bot ELABBASI>>\n", z)

    os.system('clear')

#   This code was made with love by : Mohamed El-Abbasi
#   Instagram : @mohamed__elabbasi
#   Github link : https://github.com/Melabbasi/SafeUM