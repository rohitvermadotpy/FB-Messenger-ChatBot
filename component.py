import sys
import json
import requests
from flask import Flask, request

PAT = 'your_page_access_token'


def send_message(sender_id, message_text):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

                      params={"access_token": PAT},

                      headers={"Content-Type": "application/json"},

                      data=json.dumps({
                          "recipient": {"id": sender_id},
                          "message": {"text": message_text}
                      }))


def send_img(sender_id, url):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

                      params={"access_token": PAT},

                      headers={"Content-Type": "application/json"},

                      data=json.dumps({
                          "recipient": {
                              "id": sender_id
                          },
                          "message": {
                              "attachment": {
                                  "type": "image",
                                  "payload": {
                                      "url": url
                                  }
                              }
                          }
                      }))
