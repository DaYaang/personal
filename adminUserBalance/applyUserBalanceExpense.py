import time
import requests
import json

def applyUserBalanceExpense():
    # 减向
    expenseAssetTypeIdList = [
    2,3,10,13,14,15,17,18,21,24,33,44,45,47,56,57,73,76,77,81,85,88,89,91,93,95,97,100,102,103,105,106,108,109,112,114,117,119,120,122,124,126,129,132,134,138,139,140,141,142,147,148,150,154,156,158,160,162,165,167,169,174,176,177,181,183,184,185,187,190,192,194,196,197,198,199,202,203,204,205,207,209,216,1001,1002,69,212,213,214,219
    ]
    expenseAssetTypeNameList = [
    "提现","购买","还价支付","冻结押金","解冻押金","支付租金","购买冻结","购买解冻","垫付资金","支付续租资金","支付补贴租金","求购账户提现","求购处罚","支付买断资金","支付赔付资金","支付赔偿资金","支付延期资金","支付逾期资金","支付额外赔偿","转租服务费","支付安心购","冻结安心租","支付安心租","安心租解冻","交易处罚","私密出售支出","转出到求购账户余额","求购账户余额-转出到钱包","支出安心租","支付押金保障费（特殊处理）","安心购解冻","安心购冻结","108租4免1活动支出","支付安心涨","处理买断资金","支付红锁无忧","支出红锁无忧退费","支出红锁无忧赔付","支付期数资金","处理期数资金","自动到账服务费","支付采购服务费","私密租赁补贴支出","支付极速发货","转账充值支出","冻结数码租赁押金","解冻数码租赁押金","支付数码租金","支付数码逾期违约金","支付数码强制买断","退还立减金补贴","支付租赁过户","支付租赁过户手续费","支付返现补贴","支付手机充值","支出开箱出金","支付活动资金","支付提现券资金","支付官箱自开","支出官箱自开","还价处罚","支付租赁过户返现","支付任务返现补贴","支付解封服务费","交易服务费","冻结信用超能力","解冻信用超能力","支付信用超能力","租赁服务费","购买CDK","支付赠送服务费","支付出租大会员","赔付服务费","冻结省钱会员","解冻省钱会员","支付省钱会员","退还优惠券折扣","冻结赠送服务费","解冻赠送服务费","支付自动发货","支出自动发货","支付免押增值服务","购买服饰","数据修复减","司法划拨","支付补贴","冻结预售保证金","解冻预售保证金","扣除违约金","支付预售保证金"
    ]

    # 账户类型
    accountTypeTypeIdList = [
1,2,4,5,6,7
    ]
    accountTypeTypeNameList = [
"余额1","余额2","求购充值1","求购充值2","求购转入1","求购转入2"
    ]

    # 渠道类型
    payChannelTypeIdList = [
        0,2,13,11,15
    ]
    payChannelTypeNameList = [
        "余额","支付宝","抖音","京东","易宝"
    ]

    url = "https://t1-api-intranet.youpin898.com/api/youpin/admin/adjust/submitApply"

    for i in range (0,len(expenseAssetTypeIdList)):
        for j in range (0,len(accountTypeTypeIdList)):
            for k in range(0,len(payChannelTypeIdList)):
                payload = json.dumps({
                  "relatedOrderNo": expenseAssetTypeIdList[i],
                  "payOrderNo": "",
                  "decAccountInfo": {
                    "userId": "174510",
                    "checked": True,
                    "assetType": expenseAssetTypeIdList[i],
                    "accountPayChannelType": payChannelTypeIdList[k],
                    "serviceFee": 0,
                    "itemList": [
                      {
                        "adjustAmount": expenseAssetTypeIdList[i]/100,
                        "adjustAccountType": accountTypeTypeIdList[j]
                      }
                    ]
                  },
                  "applyRemark": "减-资金明细id："+str(expenseAssetTypeIdList[i])+
                                 "  减-资金明细："+str(expenseAssetTypeNameList[i])+
                                 "  减-账户类型："+str(accountTypeTypeNameList[j])+
                                 "  调账渠道："+str(payChannelTypeNameList[k])
                })
                headers = {
                  'accept': 'application/json, text/plain, */*',
                  'accept-language': 'zh-CN,zh;q=0.9',
                  'app-id': 'business_workbench',
                  'apptype': '1',
                  'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkNGY5MzQyMjg2ZjE0MjU5ODEzMzk2ZWZiZTI5N2MyNSIsIm5hbWVpZCI6IjE2NyIsIklkIjoiMTY3IiwidW5pcXVlX25hbWUiOiJkYXlhbmcyIiwiTmFtZSI6ImRheWFuZzIiLCJuYmYiOjE3MzUwMjAyMzcsImV4cCI6MTc2NjEyNDIzNywiaXNzIjoiYWRtaW4ueW91cGluODk4LmNvbSIsImF1ZCI6ImFkbWluIn0.p2oJbeaHkPEoxBfJqNkbPd7X1ZxYYvAUY9ZeEku4MAE',
                  'cache-control': 'no-cache',
                  'content-type': 'application/json',
                  'origin': 'https://t1-uuadmin.youpin898.com',
                  'pragma': 'no-cache',
                  'priority': 'u=1, i',
                  'referer': 'https://t1-uuadmin.youpin898.com/',
                  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"macOS"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-site',
                  'sso-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxMDEwOSIsIk4iOiLliJjmtIsiLCJFRkYiOjE3MzUxMDY2NTgsIkRPTUFJTiI6InQxLXV1YWRtaW4ueW91cGluODk4LmNvbXx0ZXN0IiwiUkYiOiIwXzEwIiwiUk4iOiJQQ1kxSlYifQ.Fh6DXDXwfCm4l0rO2NT4tamvK8d9a2Ne5i_rE0HCuOM',
                  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                with open("/Volumes/yaangmac/mypthonfiles/adminUserBalance/expenseResult.txt","a+",encoding="UTF-8") as incomeResult:
                    incomeResult.write(response.request.body)
                    incomeResult.write("\n")
                    incomeResult.write(response.text)
                    incomeResult.write("\n")
                    incomeResult.write("\n")
                print(response.request.body)
                print(response.text)

applyUserBalanceExpense()
