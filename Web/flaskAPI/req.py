import sys
import requests
import json


def get_req():
    url = 'http://127.0.0.1:5000/tweet'
    res = requests.get(url)
    print(res.text)

def post_req():
    url = 'http://127.0.0.1:5000/tweet'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {"tweet": "Hello World!"}
    
    res = requests.post(url, headers=headers, data=json.dumps(data))
    print(res.text)
    
def put_req(id):
    url = f'http://127.0.0.1:5000/tweet/{id}'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {"tweet": "Change World!"}
    
    res = requests.put(url, headers=headers, data=json.dumps(data))
    print(res.text)
    
def delete_req(id):
    url = f'http://127.0.0.1:5000/tweet/{id}'
    res = requests.delete(url)
    print(res.text)
    
if __name__ == '__main__':
    args = sys.argv
    methods = args[1]
    
    if methods == 'get':
        get_req()
    elif methods == 'post':
        post_req()
    elif methods == 'put':
        put_req(args[2])
    elif methods == 'delete':
        delete_req(args[2])