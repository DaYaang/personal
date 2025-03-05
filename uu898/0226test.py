"""
@Author  : liuyang
@Time    : 2025/2/26 00:32
@Content : 
"""
import socket
import time

HOST = 'https://api.youpin898.com'
PORT = 80
headers = (
    "POST /api/homepage/v3/detail/commodity/list/lease HTTP/1.1\r\n"
    "Host: api.youpin898.com\r\n"
    "Cookie: acw_tc=0b3c7da217404969864043889e0ce5d6366245a7915edd960cb4ccd2f37b59\r\n"
    "Content-Type: application/json\r\n"
    "apptype: 3\r\n"
    "Content-Encoding: gzip\r\n"
    "DeviceToken: 2BF87BAA-EBE5-4D94-A2B0-523249D5BA9F\r\n"
    "DeviceSysVersion: 18.1.1\r\n"
    "requesttag: fa84a7bfe3f0fcda30cc13b8eefbd0b2\r\n"
    "version: 5.28.0\r\n"
    "Gameid: 730\r\n"
    "uk: 5CovRI8oo0zKfJGIxKsn7PIYEYU2oHwdNB2SFuDIzLYIfz9jK20k90dZgcCPKqT1H\r\n"
    "package-type: uuyp\r\n"
    "platform: ios\r\n"
    "Connection: keep-alive\r\n"
    "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxOGRlODE2NjRhYTQ0Y2FkYjk0NDA1NjI5ZGI3YWQ1MiIsIm5hbWVpZCI6IjE5MTA4ODYiLCJJZCI6IjE5MTA4ODYiLCJ1bmlxdWVfbmFtZSI6IllQMDAwMTkxMDg4NiIsIk5hbWUiOiJZUDAwMDE5MTA4ODYiLCJ2ZXJzaW9uIjoidkJlIiwibmJmIjoxNzM5ODgxNzY0LCJleHAiOjE3NDM3ODA1NjQsImlzcyI6InlvdXBpbjg5OC5jb20iLCJkZXZpY2VJZCI6IjJCRjg3QkFBLUVCRTUtNEQ5NC1BMkIwLTUyMzI0OUQ1QkE5RiIsImF1ZCI6InVzZXIifQ.1y2YaGnj--B9VB7TNgnZ9At-02LT4wJb0B11KMAQcnE\r\n"
    "tracestate: bnro=iOS/18.1.1_iOS/8.15.100_NSURLSession\r\n"
    "api-version: 1.0\r\n"
    "platform: ios\r\n"
    "Accept-Language: zh-Hans-OM;q=1.0, ar-OM;q=0.9\r\n"
    "traceparent: 00-0ee073643fcc40b7a5d42419da818db1-4cb2513a57531971-01\r\n"
    "app-version: 5.28.0\r\n"
    "Accept-Encoding: gzip\r\n"
    "Content-Length: 387\r\n"  # 明确指定Body长度
    "\r\n"  # 头部结束
)

body = '{"pageSize":20,"autoDelivery":0,"sortType":1,"userId":"1910886","pageIndex":1,"ultraLongLeaseMoreZones":3,"AppType":"3","templateId":108728,"stickerAbrade":0,"hasLease":"true","appVersion":"5.28.0","listType":30,"gameId":730,"Platform":"ios","SessionId":"2BF87BAA-EBE5-4D94-A2B0-523249D5BA9F","Version":"5.28.0","sortTypeKey":"LEASE_SHORT_PRICE_ASC","listSortType":2,"haveBuZhangType":0}'  # 长度12字节

# 创建Socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# 第一次发送：仅发送头部
print("Sending headers...")
s.send(headers.encode())
time.sleep(1)  # 模拟100ms延迟（实际测试时可调整）

# 第二次发送：发送Body
print("Sending body...")
s.send(body.encode())

# 接收响应
response = s.recv(1024)
print("Response:", response.decode())



s.close()
