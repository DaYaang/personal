import time
import requests
import json


# 预发环境造申请批量客户审核中数据
for i in range(5, 105):
    apply_url = "https://pre-gw-openapi.youpin898.com/custom/v1/api/customApply"

    # apply body 操作
    j = 100 + int(i)
    mobile = int(str(18112341) + str(j))
    cardId = str(221124202211240) + str(j)
    apply_data = {
        "mobile": mobile,
        "cardId": cardId,
        "cardPositive": "pre/2022/11-24/6211e95c7f5c47bba03d7b7c98a37525.png",
        "cardUnpositive": "pre/2022/11-24/6211e95c7f5c47bba03d7b7c98a37525.png",
        "orderNum": j,
        "orderTotal": j,
        "apiTotal": j,
        "cardName": "刘洋测试一"
    }
    apply_data_json = json.dumps(apply_data)
    # 将apply_data_json进行指定编码处理
    byteapply_body = apply_data_json.encode("UTF-8")

    # apply 请求头
    apply_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkZTQ4NGM2NDk3OTM0MzM5ODllOTZkNzBjMGM3ZjQ0MyIsIm5hbWVpZCI6IjE1MjkxMyIsIklkIjoiMTUyOTEzIiwidW5pcXVlX25hbWUiOiLmtYvor5XkuJPnlKgxNTI5MTMiLCJOYW1lIjoi5rWL6K-V5LiT55SoMTUyOTEzIiwibmJmIjoxNjY5NDQxMDc2LCJleHAiOjE3MDA5NzcwNzYsImlzcyI6InlvdXBpbjg5OC5jb20iLCJhdWQiOiJ1c2VyIn0.B-MN-hFtEK7zF28SzdCakC-jx-wZYBBlUr3T-yfzcus'
    }

    # 审核部分参数
    audit_url = "https://api.youpin898.com/api/youpin/admin/order/v1/api/applyAudit"

    # 审核入参body
    auditDesc = "操作理由" + str(i)
    opDesc = "拒绝理由" + str(i)
    audit_data = {
        "id": i,
        "status": "3",
        "auditDesc": auditDesc,
        "opDesc": opDesc,
        "updateBy": "1"
    }
    audit_data_json = json.dumps(audit_data)
    byteadit_body = audit_data_json.encode("UTF-8")
    audit_headers = {
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJlNTA5OWQyNThhYzY0YWM0YjkzZTM4NGE1MDY0ZmNiMiIsIm5hbWVpZCI6IjEiLCJJZCI6IjEiLCJ1bmlxdWVfbmFtZSI6ImFkbWluIiwiTmFtZSI6ImFkbWluIiwibmJmIjoxNjY5NDQyNzUwLCJleHAiOjE3MDA1NDY3NTAsImlzcyI6ImFkbWluLnlvdXBpbjg5OC5jb20iLCJhdWQiOiJhZG1pbiJ9.hbfuM8jjrpduADWoawcJj6txe4w5bQuT9HuyIWmDgxg',
        'Content-Type': 'application/json'
    }

    # 调用申请接口
    apply_response = requests.request("POST", url=apply_url, headers=apply_headers, data=byteapply_body)
    apply_response_body = apply_response.text
    print(apply_response_body)
    time.sleep(1)
    with open("/Volumes/yaangmac/testdata.txt", mode="a+", encoding="utf-8") as f:
        f.write(apply_response_body + "\n")

    # 调用审核接口进行审核拒绝
    audit_response = requests.request("POST", audit_url, headers=audit_headers, data=byteadit_body)
    aduit_response_body = audit_response.text
    print(aduit_response_body)
    with open("/Volumes/yaangmac/testdata.txt", mode="a+", encoding="utf-8") as f:
        f.write(apply_response_body + "\n")
