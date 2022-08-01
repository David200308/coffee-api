from flask import *
import json, time, os
from matplotlib.font_manager import json_dump

f = open('coffee_data.json')
data = json.load(f)

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def home_page():
    data_set = {'Page': 'Home', 'Message': 'Successful loaded the Home Page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/coffee/', methods = ['GET'])

def request_page():
    coffee_query = str(request.args.get('coffee'))

    for i in data['coffee']:
        if i["Name"] == "Latte":
            content = i["Content"]

    data_set = {'State': 'Request', 'Coffee': f'{coffee_query}', 'Coffee Content': content, 'Timestamp': time.ctime(time.time())}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port=5555)