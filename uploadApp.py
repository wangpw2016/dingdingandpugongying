#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import sys
import os
import json

app_key='1a8048cfa7d5f9882d52e59cf7887ee7'
user_key='008df7170a7ce59cb40f8319b05978ed'
# file = open(os.path.abspath(sys.argv[1]),'rb')
file = open(os.path.abspath('D:\\app\\app-debug.apk'),'rb')
uploadAppQuest = requests.post("https://www.pgyer.com/apiv2/app/upload",data={"_api_key":app_key,'uKey':user_key},files={"file": file})
uploadResult = uploadAppQuest.json()['data']['buildQRCodeURL']
print(uploadResult)

buildKey=uploadAppQuest.json()['data']['buildKey'];

params1={'_api_key': app_key  ,
        'buildKey': uploadAppQuest.json()['data']['buildKey']
         }
dataResult='https://www.pgyer.com/apiv2/app/install?_api_key={0}&buildKey={1}'.format(app_key,buildKey)
print(dataResult)
data = {
    "msgtype": "markdown",
    "markdown": {"title": "Android测试包",
                 "text": "### Android测试包 \n\n  ![二维码]({0}) \n\n #### 扫码下载 \n\n\n\n #### 复制链接下载 \n\n {1}".format(uploadResult,dataResult)
                 },
    "at": {
        "isAtAll": False
    }
}

print(data)

headers = {'Content-Type': 'application/json'}
dingdingPost = requests.post("https://oapi.dingtalk.com/robot/send?access_token=d12b71b82f3a617c6c6a4371c0a1b7fe66fbdda65bdea5a1f7c286d7eb11bcf8",data=json.dumps(data),headers=headers)
print(dingdingPost)

