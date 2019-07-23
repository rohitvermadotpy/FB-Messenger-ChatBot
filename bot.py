import sys
import json
import requests
from flask import Flask, request
import component as com

app = Flask(__name__)

VERIFY_TOKEN = 'your_token'
PAT = 'your_page_access_token'


@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"


@app.route('/', methods=['POST'])
def handle_message():
    data = request.get_json()
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    req = requests.get(
        'https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}'.format(sender_id, PAT))
    user_data = req.json()
    if user_data.get("first_name"):
        f_name = user_data["first_name"]
        l_name = user_data["last_name"]
        p_pic = user_data["profile_pic"]

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    try:
                        recipient_id = messaging_event["recipient"]["id"]
                        message_text = messaging_event["message"]["text"]

                        if message_text == "greetings":
                            com.send_message(
                                sender_id, "hello {}".format(f_name))

                        elif message_text == "send image":
                            com.send_img(sender_id, p_pic)

                        else:
                            com.send_message(
                                sender_id, "Hey I'm just a ChatBot. Wait for a real human to reply!")
                    except:
                        com.send_message(
                            sender_id, "this type of message not supported")

    return "ok"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
