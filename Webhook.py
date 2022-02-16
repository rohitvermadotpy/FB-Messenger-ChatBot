from flask import Flask, request
from Bot import echo

app = Flask(__name__)


# fb hub verification
@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == 'your_token'):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"


# fb message handling
@app.route('/', methods=['POST'])
def handle_message():
    if request.method == 'POST':
        data = request.get_json()
        if data['object'] == "page" and 'message' in data['entry'][0]['messaging'][0]:
            echo(data)
        else:
            pass
    return "ok"


# main driver function
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=80)
