#########################################################

import certifi
import urllib3

import ssl
import websocket

from enum import Enum
from getpass import getpass
import random, string, json
import threading, time
from http.client import responses

#########################################################

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

#########################################################

def posturlbody(url, headers = {}, body = ""):
    r = http.request("POST", url, headers = headers, body = body)
    content = r.data.decode("utf-8")
    return content

def read_string_from_file(path, default):
	try:
		content = open(path).read()
		return content
	except:
		return default

#########################################################

def randsri():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

def tourneychaturl(tid):
    return "wss://socket.lichess.org/tournament/{}/socket/v4?sri={}".format(tid, randsri())

#########################################################

def login(username = None, password = None):
    if not username:
        username = input("Username: ")
    if not password:
        password = getpass()

    res = http.request("POST", "https://lichess.org/login?referrer=%2F", headers = {
        "Referer": "https://lichess.org/login?referrer=%2F"
    }, fields = {
        "username": username,
        "password": password
    })

    print("login status", responses[res.status])

    if res.status == 200:
        sch = res.info().get("Set-Cookie")

        lila2 = sch.split(";")[0][6:]

        print("obtained", lila2)
        return lila2
    else:
        print("could not log in")
        return None

#########################################################

def talktourneychattarget(tid, lila2, msg):
    ws = None    

    def msgt(ws, msg):        
        ws.send(json.dumps({
            "t": "talk",
            "d": msg
        }))
        print("sent {} {}".format(tid, msg))
        ws.close()

    def on_open(x):
        nonlocal ws        
        print("opened {} {}".format(tid, msg))
        threading.Thread(target = msgt, args = (ws, msg)).start()

    def on_message(ws, msg):
        print("message", msg)

    ws = websocket.WebSocketApp(tourneychaturl(tid),        
        on_open = on_open,        
        on_message = on_message,
        cookie = "lila2={}".format(lila2)
    )

    ws.run_forever(
        host = "socket.lichess.org",
        origin = "https://lichess.org"
    )

    print("talk terminated ok {} {}".format(tid, msg))

def talktourneychat(tid, lila2, msg):
    threading.Thread(target = talktourneychattarget, args = (tid, lila2, msg)).start()

#########################################################

class MESSAGE_RESULT(Enum):
    MESSAGE_DELIVERED = 1
    MESSAGE_DECLINED = 2
    MESSAGE_FAILED = 3
    MESSAGE_FATAL = 4

def sendmessage(username, subject, message, lila2):
    url = "https://lichess.org/inbox/new?username={}".format(username)
    print("sending to {}\nsubject: {}\nmessage: {}\nurl: {}".format(username, subject, message, url))

    try:
        res = http.request("POST", url, headers = {
            "Cookie": "lila2={}".format(lila2)
        }, fields = {
            "subject": subject,
            "text": message
        })

        print("message delivery status", responses[res.status])

        try:
            #content = res.data.decode("utf-8")
            content = "{}".format(res.data)            
            if '<p class="error">' in content:
                print("message declined")
                return MESSAGE_RESULT.MESSAGE_DECLINED
            if '<div class="thread_message_body">' in content:
                print("message delivered OK")
                return MESSAGE_RESULT.MESSAGE_DELIVERED
            print("message delivery failed")
            return MESSAGE_RESULT.MESSAGE_FAILED
        except:
            print("fatal, could not process response body")
            print(res.info())
            return MESSAGE_RESULT.MESSAGE_FATAL
    except:
        print("fatal, http request failed")
        return MESSAGE_RESULT.MESSAGE_FATAL

#########################################################

def jointourney(tid, lila2):
    turl = "https://lichess.org/tournament/{}".format(tid)
    jurl = turl + "/join"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "application/vnd.lichess.v3+json",
        "Referer": turl,
        "Cookie": "lila2={}".format(lila2)        
    }
    posturlbody(jurl, headers = headers, body = '{"p": null}')

#########################################################
