import json
import re
import time
import requests
from jsonpath import jsonpath


def queryCommodity(template):
    url = "https://api.youpin898.com/api/youpin/commodity/commodity/detail/commodity/list/Lease/transfer"

    payload = json.dumps({
	"autoDelivery": 0,
	"compensationType": "ULTRA_LONG_FIX",
	"hasLease": "true",
	"haveBuZhangType": 0,
	"leaseTransferMaxPrice": "",
	"leaseTransferMinPrice": "",
	"listSortType": "2",
	"listType": 30,
	"mergeFlag": 0,
	"pageIndex": 1,
	"pageSize": 50,
	"presaleMoreZones": 0,
	"sortType": "1",
	"sortTypeKey": "SELL_DEFAULT",
	"sourceChannel": "",
	"status": "20",
	"stickerAbrade": 0,
	"stickersIsSort": False,
	"templateId": {template},
	"ultraLongLeaseMoreZones": 0,
	"userId": "1908872",
	"Sessionid": "Z8ADfJkzRJcDACZBOHcTgkuW"
})
    headers = {
      'br_interactive_uuid': '63e7464c-e32e-4eef-af69-cc0c6cd7e317',
      'DeviceToken': 'Z8ADfJkzRJcDACZBOHcTgkuW',
      'DeviceId': 'Z8ADfJkzRJcDACZBOHcTgkuW',
      'requestTag': 'BB73709EF4EA56885A6CE8B0F0C4C076',
      'Gameid': '730',
      'deviceType': '1',
      'platform': 'android',
      'currentTheme': 'Light',
      'package-type': 'uuyp',
      'App-Version': '5.28.3',
      'uk': '5CjtWLic10d1jecCNLpQYGiNpOtCFmbOb7kmuz7PYgwCOc5BNXSwPXdMzkDRkCb1L',
      'Device-Info': '{"deviceId":"Z8ADfJkzRJcDACZBOHcTgkuW","deviceType":"23116PN5BC","hasSteamApp":1,"requestTag":"BB73709EF4EA56885A6CE8B0F0C4C076","systemName ":"Android","systemVersion":"15"}',
      'AppType': '4',
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyN2QxZDljNjQyZTQ0NTA4ODEwOWJkZDBlMjUwM2FmNyIsIm5hbWVpZCI6IjE5MDg4NzIiLCJJZCI6IjE5MDg4NzIiLCJ1bmlxdWVfbmFtZSI6IllQMDAwMTkwODg3MiIsIk5hbWUiOiJZUDAwMDE5MDg4NzIiLCJ2ZXJzaW9uIjoiRzQwIiwibmJmIjoxNzQwNjM4NjMxLCJleHAiOjE3NDU2OTY2MzEsImlzcyI6InlvdXBpbjg5OC5jb20iLCJkZXZpY2VJZCI6Ilo4QURmSmt6UkpjREFDWkJPSGNUZ2t1VyIsImF1ZCI6InVzZXIifQ.oIKJWaY6MSyRlGQQ0a_wED-5fvp3X16ZMqrKLlv8py4',
      'Content-Type': 'application/json; charset=utf-8',
      'Host': 'api.youpin898.com',
      'User-Agent': 'okhttp/3.14.9',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'Cookie': 'acw_tc=0b3c7da217406880540434729e0ccb7e34343c610083decc614629fa054e82'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    resJson = response.json()
    commodityInfoList = jsonpath(resJson,"$..commodityInfoList")[0]
    commodityid_list = []
    if commodityInfoList is not None:
         if len(commodityInfoList) > 1:
             for i in range(0,len(commodityInfoList)):
                commodityid = jsonpath(commodityInfoList[i],"$.id")
                commodityid_list.append(commodityid[0])
    print(commodityid_list)

    for commodityid_id in commodityid_list:
        url1 = "https://api.youpin898.com/api/youpin/bff/new/commodity/v1/commodity/lease-transfer-info"
        payload1 = json.dumps({"commodityId":commodityid_id,"bizType":4006})
        headers1 = {
          'Host': 'api.youpin898.com',
          'appType': '3',
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 uuyp/uk=5CovRI8oo0zKfJGIxKsn7PIYEYU2oHwdNB2SFuDIzLYIfz9jK20k90dZgcCPKqT1H&uid=2452393&appVersion=5.28.0&package-type=uuyp&currentTheme=System&platform=iOS',
          'Referer': 'https://hybrid.youpin898.com/',
          'deviceToken': '2BF87BAA-EBE5-4D94-A2B0-523249D5BA9F',
          'App-Source': 'h5',
          'Origin': 'https://hybrid.youpin898.com',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Site': 'same-site',
          'uk': '5CovRI8oo0zKfJGIxKsn7PIYEYU2oHwdNB2SFuDIzLYIfz9jK20k90dZgcCPKqT1H',
          'package-type': 'uuyp',
          'platform': 'ios',
          'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0NjVjYzNmMWJlN2U0NmE0OWIwOTA1NmZkMGE0MTRhZSIsIm5hbWVpZCI6IjI0NTIzOTMiLCJJZCI6IjI0NTIzOTMiLCJ1bmlxdWVfbmFtZSI6IuWls-Wkp-WtpueUn-WcqOe6v-enkuWPkSIsIk5hbWUiOiLlpbPlpKflrabnlJ_lnKjnur_np5Llj5EiLCJ2ZXJzaW9uIjoieHhYIiwibmJmIjoxNzM5Nzc3MzExLCJleHAiOjE3NDMwNjA1MTEsImlzcyI6InlvdXBpbjg5OC5jb20iLCJkZXZpY2VJZCI6IjJCRjg3QkFBLUVCRTUtNEQ5NC1BMkIwLTUyMzI0OUQ1QkE5RiIsImF1ZCI6InVzZXIifQ.o4o-OsG9NcE2s_GXc_uiAv1j3VfatIC2O31rP8ys6q4',
          'tracestate': 'bnro=iPhone/18_1_1_js/2.2.2_xhr_XMLHttpRequest',
          'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
          'Accept': 'application/json, text/plain, */*',
          'Content-Type': 'application/json;charset=utf-8',
          'App-Version': '5.28.0',
          'traceparent': '00-f9c0c766327e72ad0da6f03d1d2b2200-a01d28e71c6f3fd4-01',
          'Sec-Fetch-Mode': 'cors',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Cookie': 'acw_tc=0b3c7da217397810750963210e0cf02c89a3a57a48b1470ad7f4c200bcfa8c'
        }

        response1 = requests.request("POST", url1, headers=headers1, data=payload1)
        # 匹配赔付金额
        res_json = response1.json()
        protocolDesc = jsonpath(res_json,"$..protocolDesc")
        match = re.search(r'固定赔付\d+.\d+', protocolDesc[0])
        claim = match.group(0)
        # claim = protocolDesc
        # 获取拼接数据
        commodityName = jsonpath(res_json,"$..commodityName")[0]
        commodityAbrade = jsonpath(res_json,"$..commodityAbrade")[0]
        commodityConversionPrice = jsonpath(res_json,"$..commodityConversionPrice")[0]
        hasLeasedDays =  jsonpath(res_json,"$..hasLeasedDays")[0]
        leaseDays =  jsonpath(res_json,"$..leaseDays")[0]
        with open("data.txt","a") as datatex:
            dateanser = f"名称：{commodityName}-磨损度：{commodityAbrade}-租赁进度：{hasLeasedDays}/{leaseDays}-{claim}-过户价格：{commodityConversionPrice}\n"
            datatex.write(dateanser)

        print(f"写入商品{commodityid_id}信息结束")
        time.sleep(1)
    print(f"模版{template}查询结束")

    print(response.text)



idlit_knife = [166,267,275,294,297,402,409,411,487,490,562,604,647,739,754,892,936,1019,1086,1226,1244,1484,1533,1678,1679,1681,1708,1785,1809,1870,1904,1956,1967,1980,1986,2000,2025,2026,2049,2122,2134,2298,2386,2413,2521,2565,2629,2663,2752,2754,2787,2788,2791,2803,2885,2940,2944,2957,2967,2969,2975,2980,3007,3109,3237,3242,3467,3574,3745,3803,3874,3881,4092,4292,4298,4299,4360,4361,4423,4487,4533,4665,5243,5264,5266,5271,5286,5362,5376,5407,5465,5582,5718,5870,5882,5925,5953,6201,6335,6339,6836,6992,7483,8973,9009,9512,9514,9538,9567,9935,9936,9975,10397,10645,10843,10990,10994,11209,12359,12936,13158,13173,14606,14617,14618,14626,14717,14799,32982,34683,34774,34782,34967,34973,35222,35223,35226,35229,35231,36720,36841,36843,36905,36939,37036,37120,42968,43284,43338,43339,43416,43450,43517,43529,43531,43535,43574,43578,43591,43630,43631,43632,43665,43676,43679,43690,43691,43692,43695,43705,43713,43786,43803,43805,43807,43810,43811,43813,43841,43846,43855,43892,43894,43895,43918,43951,43963,44022,44029,44035,44038,44066,44076,44082,44087,44191,44195,44196,44209,44221]

for id in idlit_knife:
    queryCommodity(id)
