import time

import requests

def resetUserState():
    url = "https://preapi-intranet.youpin898.com/api/youpin/api/admin/User/ModifyUserRiskStatus"

    payload1 = "{\"UserId\":152942,\"RiskStatus\":0,\"Reason\":\"\"}"
    payload2 = "{\"UserId\":152945,\"RiskStatus\":0,\"Reason\":\"\"}"
    payload3= "{\"UserId\":90003005,\"RiskStatus\":0,\"Reason\":\"\"}"
    # payload4= "{\"UserId\":152942,\"RiskStatus\":0,\"Reason\":\"\"}"


    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'zh-CN,zh;q=0.9',
      'app-id': 'business_workbench',
      'apptype': '1',
      'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkYjUyZmIxOTUxMTI0YzI5ODBlNmFmOWYxNzdmODJiMCIsIm5hbWVpZCI6IjUzIiwiSWQiOiI1MyIsInVuaXF1ZV9uYW1lIjoi5YiY5rSLIiwiTmFtZSI6IuWImOa0iyIsIm5iZiI6MTczMzczNzExNCwiZXhwIjoxNzY0ODQxMTE0LCJpc3MiOiJhZG1pbi55b3VwaW44OTguY29tIiwiYXVkIjoiYWRtaW4ifQ.qhVFHQeR6DSD0ZbSA3C9-jWRZasHQUnXM3ZnTane3eA',
      'cache-control': 'no-cache',
      'content-type': 'application/json;charset=UTF-8',
      'origin': 'https://uuadminpre.youpin898.com',
      'pragma': 'no-cache',
      'priority': 'u=1, i',
      'referer': 'https://uuadminpre.youpin898.com/',
      'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'sso-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxMDEwOSIsIk4iOiLliJjmtIsiLCJFRkYiOjE3MzM4MjM1MTIsIkRPTUFJTiI6InV1YWRtaW5wcmUueW91cGluODk4LmNvbXxwcmUiLCJSRiI6IjBfMTAiLCJSTiI6ImJ0WkJBZyJ9.VY19bz4V4ofYMZMgqD-Y-wkgaaBMTsVMeWIr225bAC8',
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response1 = requests.request("PUT", url, headers=headers, data=payload1,verify=False)
    print(response1.text)
    response2 = requests.request("PUT", url, headers=headers, data=payload2,verify=False)
    print(response2.text)
    response3 = requests.request("PUT", url, headers=headers, data=payload3,verify=False)
    print(response3.text)
    # response4 = requests.request("PUT", url, headers=headers, data=payload4,verify=False)
    # print(response4.text)

resetUserState()

while True:
    resetUserState()
    time.sleep(60)
