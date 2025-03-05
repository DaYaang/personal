import time
import requests
import json

def applyUserBalance():
    # 增向
    incAccountTypeIdList = [
        1,4,5,6,11,13,14,16,17,18,22,23,25,34,43,46,48,49,54,55,58,71,72,74,75,78,82,83,86,87,88,90,91,92,94,96,98,99,101,104,105,106,107,110,111,113,115,116,118,121,123,125,127,128,133,135,136,137,138,139,143,144,145,146,149,151,155,157,159,161,163,164,166,168,170,171,172,173,175,180,182,183,184,186,188,189,191,193,195,197,198,200,201,203,204,206,208,210,211,217,1000,70,212,213,215,218,220
        ]
    incAccountTypeNameList = [
        "充值","退款","出售","交易补偿","还价退款","冻结押金","解冻押金","收取租金","购买冻结","购买解冻","追回资金","提现退款","收取续租资金","退还补贴租金","求购账户充值","求购补偿","收取买断资金","退还买断资金","收取赔付资金","收取赔偿租金","押金额外扣除","退还守约资金","收取延期资金","收取逾期资金","收取额外赔偿","退还续租资金","平台账户充值","退还金额","安心购退款","安心购收取","冻结安心租","安心租收取","安心租解冻","安心租退还","私密出售补贴","求购提现退款","钱包-转出到求购账户余额","转出到钱包","安心租赔付","退还押金保障费","安心购解冻","安心购冻结","租4免1活动补贴","退还安心涨","暂收买断资金","收取安心涨","退还红锁无忧","收取红锁无忧","红锁无忧赔付","暂收期数资金","退还期数资金","收取自动到账服务费","收取采购服务费","私密租赁补贴","退还极速发货","转账充值到账","收取附加价值赔付","赔饰品差额调拨","冻结数码租赁押金","解冻数码租赁押金","退还数码租金","退还数码逾期违约金","退还数码强制买断","立减金补贴","收取租赁过户","退还租赁过户","返现补贴","退还手机充值","收取开箱出金","退还活动资金","退还提现券资金","退还求购处罚","收取官箱自开","退还官箱自开","还价补偿","退还还价处罚","收取待结租金","租赁过户返现","任务返现补贴","退还解封服务费","退还交易服务费","冻结信用超能力","解冻信用超能力","信用超能力退还","退还租赁服务费","赔饰品追回","CDK退款","退还赠送服务费","退还出租大会员","冻结省钱会员","解冻省钱会员","退还省钱会员","优惠券抵扣","冻结赠送服务费","解冻赠送服务费","收取自动发货","退还自动发货","退还免押增值服务","余额补偿入金","服饰退款","数据修复加","收取补贴","冻结预售保证金","解冻预售保证金","补贴违约金","预售违约手续费","退还预售保证金"
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

    timestr1 = str(int(time.time()))
    print(timestr1+"1")

    url = "https://t1-api-intranet.youpin898.com/api/youpin/admin/adjust/submitApply"
    for i in range (0,len(incAccountTypeIdList)):
        # for j in range (0,len(accountTypeTypeIdList)):
        #     for k in range(0,len(payChannelTypeIdList)):
                payload = json.dumps({
                  "relatedOrderNo": incAccountTypeIdList[i],
                  "payOrderNo": "",
                  "incAccountInfo": {
                    "userId": "174192",
                    "checked": True,
                    "assetType": incAccountTypeIdList[i],
                    "accountPayChannelType": payChannelTypeIdList[0],
                    "serviceFee": 0,
                    "itemList": [
                      {
                        "adjustAmount": incAccountTypeIdList[i]/100,
                        "adjustAccountType": accountTypeTypeIdList[0]
                      }
                    ]
                  },
                  "applyRemark": "增-资金明细id："+str(incAccountTypeIdList[i])+
                                 "  增-资金明细："+str(incAccountTypeNameList[i])+
                                 "  增-账户类型："+str(accountTypeTypeNameList[0])+
                                 "  调账渠道："+str(payChannelTypeNameList[0])
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
                with open("/Volumes/yaangmac/mypthonfiles/adminUserBalance/incomeResultOnly.txt","a+",encoding="UTF-8") as incomeResult:
                    incomeResult.write(response.request.body)
                    incomeResult.write("\n")
                    incomeResult.write(response.text)
                    incomeResult.write("\n")
                    incomeResult.write("\n")
                print(response.request.body)
                print(response.text)

applyUserBalance()

