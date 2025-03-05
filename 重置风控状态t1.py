import time

import requests

def resetUserState():
    url = "https://t1-api-intranet.youpin898.com/api/admin/User/ModifyUserRiskStatus"

    payload1 = "{\n    \n    \"UserId\": 173915,\n    \"RiskStatus\": 0,\n    \"Reason\": \"\"\n}"
    payload2 = "{\n    \n    \"UserId\": 175113,\n    \"RiskStatus\": 0,\n    \"Reason\": \"\"\n}"
    payload3 = "{\n    \n    \"UserId\": 173917,\n    \"RiskStatus\": 0,\n    \"Reason\": \"\"\n}"


    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'zh-CN,zh;q=0.9',
      'apptype': '1',
      'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2ODUwYjQzOTZjYTA0ZTAxOTM0Mjc1OTUxNGQxNDAyOSIsIm5hbWVpZCI6IjEwNyIsIklkIjoiMTA3IiwidW5pcXVlX25hbWUiOiLliJjmtIsiLCJOYW1lIjoi5YiY5rSLIiwibmJmIjoxNzMwMTAxMTAzLCJleHAiOjE3NjEyMDUxMDMsImlzcyI6ImFkbWluLnlvdXBpbjg5OC5jb20iLCJhdWQiOiJhZG1pbiJ9.l9OpNJv6z26RsO6hLz34ayFfWSFL6VGfyxiLdcEk-Ns',
      'cache-control': 'no-cache',
      'content-type': 'application/json;charset=UTF-8',
      'origin': 'https://t1-uuadmin.youpin898.com',
      'pragma': 'no-cache',
      'priority': 'u=1, i',
      'referer': 'https://t1-uuadmin.youpin898.com/',
      'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
      'sso-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxMDEwOSIsIk4iOiLliJjmtIsiLCJFRkYiOjE3MzM4MjM1MTIsIkRPTUFJTiI6InV1YWRtaW5wcmUueW91cGluODk4LmNvbXxwcmUiLCJSRiI6IjBfMTAiLCJSTiI6ImJ0WkJBZyJ9.VY19bz4V4ofYMZMgqD-Y-wkgaaBMTsVMeWIr225bAC8',
    }

    response1 = requests.request("PUT", url, headers=headers, data=payload1,verify=False)
    print(response1.text)
    response2 = requests.request("PUT", url, headers=headers, data=payload2,verify=False)
    print(response2.text)
    response3 = requests.request("PUT", url, headers=headers, data=payload3,verify=False)
    print(response3.text)

resetUserState()

while True:
    resetUserState()
    time.sleep(20)
