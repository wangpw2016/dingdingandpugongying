# coding: utf-8
import os
import json
import sys

#fix 中文乱码
reload(sys)
sys.setdefaultencoding('utf-8')
app_key='1a8048cfa7d5f9882d52e59cf7887ee7'
user_key='008df7170a7ce59cb40f8319b05978ed'
ipo_path='/user/wpw'
def uploadAPK():
	upload_cmd= "curl -F \"file=@"+"{0}"+"\" -F \"uKey={1}\" -F \"_api_key={2}\" -F \"updateDescription=$UpdateDescription\" https://qiniu-storage.pgyer.com/apiv1/app/upload".format(ipo_path,user_key,app_key)
	print upload_cmd

	content = os.popen(upload_cmd).read()
	return content

def send_appQRCodeURL_to_dingtalk():
	upload_result = uploadAPK();
	data = json.loads(upload_result);
	# 配置发送dingtalk通知的请求参数
	body = {}
	link = {}
	link['title'] = "测试提醒，不用理会"
	link['text'] = os.environ["UpdateDescription"]
	link['picUrl']= data['data']['appQRCodeURL']
	link['messageUrl']="蒲公英二维码所在链接"
	body['link'] = link
	body['msgtype'] = 'link'
	dataJson = json.dumps(body)
	# res = send_dingtalk_message(dataJson)
	# print(res.text)
	url = "https://oapi.dingtalk.com/robot/send?access_token="+os.environ["access_token"]
	send_cmd = "curl -H \'Content-Type: application/json\' -d \'"+dataJson+"\' "+url
	resp = os.popen(send_cmd).read()
	print resp

send_appQRCodeURL_to_dingtalk()
