import requests
import json

def send_message(message, webhook_key):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={webhook_key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        if result['errcode'] == 0:
            print("消息发送成功")
            return True
        else:
            print(f"消息发送失败: {result['errmsg']}")
            return False
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return False