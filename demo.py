import requests
import os
url = 'https://qmsg.zendee.cn/send/617ff134fba3e73a86cad1cf56ed4c5d'
response = requests.get('http://wttr.in/baoqing?format=4')
response = requests.post(url,data = {'msg': response.text})
print(response.text)
env_list = os.environ
print(env_list.get('SNOW'))
