import requests
import os
env_list = os.environ
#response = requests.get('http://wttr.in/baoqing?format=4')
response = requests.post(env_list.get('QMSG_API'),data = {'msg': '测试消息啊'})

