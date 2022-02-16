import json
import requests
import time


class com:
    def __init__(self, token):
        self.token = token

    def markMessageRead(self, uid):
        r = requests.post("https://graph.facebook.com/v12.0/me/messages",

                          params={"access_token": self.token},

                          headers={"Content-Type": "application/json"},

                          data=json.dumps({
                              "recipient": {
                                  "id": uid
                              },
                              "sender_action": "mark_seen"
                          }))

    def __senderAction(self, uid, action):
        r = requests.post("https://graph.facebook.com/v12.0/me/messages",

                          params={"access_token": self.token},

                          headers={"Content-Type": "application/json"},

                          data=json.dumps({
                              "recipient": {
                                  "id": uid
                              },
                              "sender_action": action
                          }))

    def sendmsg(self, uid, response):
        self.__senderAction(uid, 'typing_on')
        time.sleep(1)
        self.__senderAction(uid, 'typing_off')
        r = requests.post("https://graph.facebook.com/v12.0/me/messages",

                          params={"access_token": self.token},

                          headers={"Content-Type": "application/json"},

                          data=json.dumps({
                              "recipient": {"id": uid},
                              "message": response
                          }))

    def parse(self, data):
        uid = data['entry'][0]['messaging'][0]['sender']['id']
        text = data['entry'][0]['messaging'][0]['message']['text']
        return{
            "uid": uid,
            "text": text
        }
