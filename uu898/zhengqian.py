"""
@Author  : liuyang
@Time    : 2025/2/17 15:01
@Content : 
"""
import re
import time
import requests
import json
from jsonpath import jsonpath


def list_Lease_transfer(template):
    print(template)
    url = "https://api.youpin898.com/api/youpin/commodity/commodity/detail/commodity/list/Lease/transfer"
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
	"templateId": template,
	"ultraLongLeaseMoreZones": 0,
	"userId": "1908872",
	"Sessionid": "Z8ADfJkzRJcDACZBOHcTgkuW"
})

    response = requests.request("POST", url, headers=headers, data=payload)
    resjson = response.json()
    commodityInfoList = jsonpath(resjson,"$..commodityInfoList")[0]
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

def running(list_data):
    for template_id in list_data:
        print(template_id)
        list_Lease_transfer(template_id)



idlit_knife = [166,267,275,294,297,402,409,411,487,490,562,604,647,739,754,892,936,1019,1086,1226,1244,1484,1533,1678,1679,1681,1708,1785,1809,1870,1904,1956,1967,1980,1986,2000,2025,2026,2049,2122,2134,2298,2386,2413,2521,2565,2629,2663,2752,2754,2787,2788,2791,2803,2885,2940,2944,2957,2967,2969,2975,2980,3007,3109,3237,3242,3467,3574,3745,3803,3874,3881,4092,4292,4298,4299,4360,4361,4423,4487,4533,4665,5243,5264,5266,5271,5286,5362,5376,5407,5465,5582,5718,5870,5882,5925,5953,6201,6335,6339,6836,6992,7483,8973,9009,9512,9514,9538,9567,9935,9936,9975,10397,10645,10843,10990,10994,11209,12359,12936,13158,13173,14606,14617,14618,14626,14717,14799,32982,34683,34774,34782,34967,34973,35222,35223,35226,35229,35231,36720,36841,36843,36905,36939,37036,37120,42968,43284,43338,43339,43416,43450,43517,43529,43531,43535,43574,43578,43591,43630,43631,43632,43665,43676,43679,43690,43691,43692,43695,43705,43713,43786,43803,43805,43807,43810,43811,43813,43841,43846,43855,43892,43894,43895,43918,43951,43963,44022,44029,44035,44038,44066,44076,44082,44087,44191,44195,44196,44209,44221]
hot_list_100 = [
    "34966",
    "1627",
    "108533",
    "740",
    "103200",
    "918",
    "102348",
    "7548",
    "44316",
    "14798",
    "43516",
    "101025",
    "108577",
    "606",
    "109579",
    "34833",
    "407",
    "1644",
    "413",
    "1572",
    "1414",
    "108615",
    "1971",
    "9760",
    "3795",
    "101012",
    "43663",
    "6411",
    "3841",
    "109918"
]
hot_list_1000 = [
    "606",
    "34833",
    "1572",
    "108615",
    "43663",
    "1243",
    "4425",
    "44700",
    "1678",
    "109829",
    "34713",
    "109914",
    "43397",
    "108692",
    "862",
    "861",
    "10102",
    "44191",
    "51833",
    "2791",
    "2614",
    "34774",
    "45026",
    "108650",
    "108617",
    "108696",
    "108671",
    "14611",
    "743",
    "44787"
]
hot_list_10000 = [
    "754",
    "1785",
    "892",
    "34967",
    "62035",
    "44458",
    "47847",
    "46429",
    "44829",
    "62272",
    "43803",
    "62037",
    "47079",
    "54427",
    "48778",
    "45985",
    "100348",
    "43529",
    "1980",
    "3109",
    "44280",
    "47033",
    "43800",
    "2803",
    "13177",
    "5000",
    "47046",
    "62270",
    "52557",
    "62268"
]
zhedao_list = [
    49591,
    10990,
    51888,
    51233,
    47089,
    44945,
    56603,
    5870,
    47151,
    48546,
    49502,
    48869,
    52649,
    60974,
    49752,
    6992,
    60984,
    58395,
    56413,
    2752,
    51183,
    56660,
    56543,
    58084,
    52729,
    52935,
    55590,
    44946,
    44695,
    50554,
    56951,
    57049,
    60967,
    51820,
    60944,
    60949,
    45374,
    55497,
    60976,
    52648,60937,
    58440,
    52846,
    49501,
    60938,
    54312,
    53040,
    50883,
    60958,
    60983,
    60957,
    57107,
    60963,
    48345,
    103452,
    57092,
    60943,
    53820,
    104357,
    49591,
    61017,
    54684,
    60977,
    61013,
    61015,
    49524,
    57747,
    44472,
    56024,
    57839,
    60955,
    60970,
    50757,
    60975,
    60999,
    57043,
    60950,
    52744,
    60930,
    60994,58043,
    61034,
    61037,
    60997,
    61000,
    53758,
    47513,
    61009,
    61027,
    61016,
    61003,
    60978,
    104354,
    60956,
    61010,
    58330,
    61018,
    60973,
    61012,
    60998,
    61019,
    44965,
    61014,
    61008,
    60929,
    60996,
    2975,
    60948,
    57561,
    61038,
    60972,
    103450,
    57154,
    61035,
    57836,
    104390,
    61004,
    58251,
    61001,
    61028
]
wandao_list = [
    57174,
    59994,
    101415,
    101419,
    58135,
    59993,
    53709,
    59915,
    58263,
    55070,
    100356,
    100352,
    62063,
    43705,
    59984,
    59938,
    59911,
    44703,
    56009,
    59927,
    58104,
    48331,
    1708,
    57835,
    62047,
    45191,
    100366,
    62052,
    47371,
    104366,
    56882,
    54928,
    62060,
    56663,
    58389,
    58044,
    57431,
    52133,
    47282,
    48527,
    62048,
    44368,
    59961,
    59952,
    58174,
    62062,
    62055,
    62070,
    62053,
    59983,
    62046,
    53047,
    48078,
    56647,
    53497,
    50208,
    56581,
    45628,
    52158,
    104365,
    59932,
    100386,
    62051,
    62068,
    4298,
    62059,
    59972,
    101633,
    48214,
    62072,
    100404,
    54157,
    104356,
    100395,
    52191,
    101371,
    59997,
    14626,
    100398,
    59990,
    59964,
    59958,
    58350,
    62069,
    62073,
    2969,
    100376,
    59992,
    59982,
    53010,
    59954,
    57720,
    62058,
    62061,
    62065,
    57818,
    57955,
    44884,
    54404,
    51335
]
M9_list  =[
    13173,
    52149,
    754,
    2025,
    44900,
    43803,
    44808,
    45083,
    43963,
    45798,
    53307,
    4299,
    44035,
    51627,
    47847,
    43805,
    1986,
    52565,
    57052,
    43695,
    49372,
    44678,
    60443,
    50194,
    34973,
    52773,
    44444,
    46541,
    48483,
    46089,
    52805,
    56279,
    46169,
    44221,
    56579,
    44436,
    51879,
    47044,
    52888,
    48265,
    58097,
    50659,
    55258,
    47523,
    43690,
    2413,
    44029,
    60451,
    50222,
    52733,
    51803,
    51932,
    56619,
    52667,
    45197,
    47537,
    51395,
    45027,
    52180,
    48943,
    48778,
    52552,
    57781,
    44905,
    60470,
    2122,
    52545,
    52710,
    45210,
    52551,
    52891,
    51383,
    51961,
    47836,
    54397,
    52775,
    49098,
    51490,
    56300,
    52763,
    48514,
    54930,
    56596,
    46790,
    52555,
    57044,
    57718,
    51690,
    45156,
    56160,
    49081,
    57256,
    52557,
    53375,
    52931,
    55778,
    55055,
    44784,
    60392,
    56454
]
hulie_list = [
    62034,
    62041,
    62272,
    62043,
    50524,
    43450,
    45985,
    54652,
    34967,
    2803,
    100369,
    54547,
    62028,
    62044,
    2026,
    892,
    46090,
    297,
    62045,
    6201,
    2629,
    739,
    62032,
    48594,
    36720,
    100348,
    1980,
    62274,
    9567,
    62035,
    48059,
    57200,
    62038,
    46966,
    62029,
    45648,
    52725,
    62033,
    44458,
    54900,
    51930,
    62031,
    3109,
    43578,
    43591,
    44500,
    45759,
    47620,
    47867,
    44614,
    2787,
    43786,
    44763,
    44262,
    62030,
    62037,
    46348,
    57874,
    4092,
    48854,
    62039,
    3007,
    54680,
    12359,
    100350,
    51995,
    51818,
    48853,
    35222,
    55604,
    56100,
    59895,
    50046,
    44082,
    14617,
    100347,
    43811,
    100372,
    45202,
    62042,
    5882,
    49117,
    100359,
    55500,
    12936,
    53556,
    62036,
    46087,
    54739,
    43713,
    52885,
    100368,
    101320,
    55898,
    55636,
    59901,
    50826,
    62021,
    100358,
    48455
]
xiongdao_list = [
    1678,
    4665,
    48763,
    43807,
    44366,
    43338,
    46736,
    45632,
    275,
    44335,
    3745,
    46777,
    50170,
    48648,
    9538,
    43665,
    50014,
    44267,
    48499,
    43631,
    44700,
    48420,
    48338,
    56857,
    3874,
    50292,
    47140,
    103456,
    48176,
    48487,
    53690,
    14717,
    48563,
    48346,
    56766,
    45360,
    51709,
    53271,
    44759,
    53169,
    48186,
    56312,
    52799,
    51119,
    44928,
    49691,
    44521,
    54173,
    45775,
    49207,
    47516,
    46112,
    52164,
    36905,
    52028,
    53943,
    52202,
    54618,
    49881,
    50057,
    53707,
    9975,
    50886,
    55292,
    53135,
    47722,
    56592,
    48986,
    53822,
    51880,
    60885,
    50236,
    53308,
    58319,
    58147,
    51219,
    54391,
    50670,
    49659,
    52066,
    60903,
    60901,
    54213,
    55532,
    53330,
    58352,
    55588,
    52793,
    60869,
    57662,
    55534,
    60913,
    58091,
    60917,
    60874,
    58417,
    52233,
    60921,
    54583,
    55710
]
lieshazhebishou_list = [
    62006,
    61997,
    62003,
    61988,
    62014,
    47747,
    61994,
    58190,
    62007,
    45749,
    61993,
    44939,
    62000,
    62001,
    51033,
    57253,
    62004,
    62008,
    62011,
    61999,
    44730,
    62009,
    45439,
    44363,
    60323,
    54317,
    54351,
    60276,
    50660,
    49690,
    62013,
    53914,
    100391,
    62012,
    54389,
    61983,
    60275,
    55611,
    58246,
    61996,
    53566,
    55182,
    109496,
    61998,
    100397,
    100353,
    53179,
    5243,
    61984,
    62010,
    58157,
    57525,
    60278,
    100377,
    60330,
    61986,
    58333,
    51929,
    54821,
    53120,
    100364,
    60319,
    60352,
    60297,
    62005,
    55711,
    56365,
    101631,
    60318,
    60298,
    45325,
    60322,
    58015,
    57698,
    56684,
    100381,
    101383,
    62002,
    54359,
    100361,
    58483,
    61985,
    60315,
    101411,
    52653,
    60358,
    60283,
    100360,
    60279,
    57222,
    100402,
    57939,
    60344,
    60310,
    56636,
    56818,
    52808,
    60277,
    100346,
    60292
]
chuangchang_list = [
    10994,
    51630,
    44038,
    48167,
    5286,
    43339,
    13158,
    43416,
    52184,
    46600,
    50930,
    1484,
    55084,
    52859,
    53183,
    57190,
    51453,
    53079,
    53548,
    60152,
    45171,
    45958,
    58172,
    49948,
    48246,
    48571,
    35229,
    56142,
    48488,
    51165,
    44351,
    53441,
    56258,
    60167,
    57821,
    49813,
    60153,
    57946,
    52734,
    60188,
    52989,
    60186,
    51998,
    60228,
    60156,
    60249,
    55181,
    46122,
    60125,
    46567,
    49195,
    49664,
    57357,
    56574,
    60174,
    49036,
    48989,
    60185,
    55909,
    60162,
    45920,
    51870,
    53029,
    60132,
    60158,
    58024,
    53490,
    51971,
    56626,
    60263,
    60169,
    57634,
    58458,
    60130,
    56817,
    51244,
    57687,
    58113,
    60145,
    56529,
    60160,
    103439,
    56668,
    58146,
    60205,
    60161,
    60190,
    57981,
    60155,
    56443,
    58078,
    58472,
    57378,
    57391,
    60195,
    60191,
    60129,
    51617,
    55295,
    60219
]
anyingshuangbi = [
    61941,
    61936,
    55947,
    44894,
    35226,
    61954,
    2940,
    51156,
    60684,
    61938,
    61923,
    61940,
    61957,
    61947,
    45931,
    46726,
    35223,
    6335,
    45051,
    51121,
    61931,
    61958,
    46571,
    52705,
    45516,
    52311,
    61944,
    61946,
    61953,
    61943,
    60696,
    52940,
    61933,
    61949,
    61922,
    56191,
    61942,
    10645,
    56707,
    53302,
    61926,
    54687,
    61952,
    61925,
    36841,
    60678,
    55761,
    61950,
    61956,
    50447,
    57407,
    61951,
    50323,
    60666,
    45921,
    56735,
    51144,
    61924,
    61955,
    57994,
    50384,
    60703,
    61929,
    55277,
    60686,
    43632,
    101630,
    61945,
    57399,
    51894,
    61948,
    60738,
    60700,
    100393,
    60688,
    57465,
    60699,
    51125,
    60697,
    100374,
    58168,
    50990,
    49088,
    47943,
    60677,
    61934,
    57110,
    61937,
    57753,
    50914,
    60747,
    61939,
    100406,
    60712,
    101324,
    60704,
    58411,
    60777,
    60698,
    57457
]
duanjian = [
    49076,
    48665,
    4487,
    44191,
    46917,
    45912,
    51332,
    1679,
    54589,
    5718,
    51790,
    48179,
    45278,
    45635,
    44735,
    50121,
    46108,
    44259,
    52303,
    2791,
    54811,
    5925,
    60827,
    54677,
    50326,
    57039,
    49099,
    44307,
    55428,
    58373,
    52142,
    55279,
    2957,
    50879,
    45789,
    53301,
    47051,
    56999,
    50612,
    60840,
    45586,
    54955,
    43676,
    48308,
    52220,
    43284,
    49007,
    47770,
    5362,
    53670,
    48590,
    51249,
    52870,
    52586,
    51097,
    49952,
    56998,
    48410,
    58268,
    60851,
    60829,
    57273,
    2386,
    49742,
    57404,
    53664,
    51858,
    55468,
    55280,
    55082,
    60843,
    45679,
    56062,
    57808,
    54604,
    51118,
    60838,
    57512,
    52189,
    60779,
    48533,
    55498,
    58400,
    57220,
    57188,
    53167,
    51206,
    56455,
    58123,
    60850,
    56711,
    56591,
    60784,
    58469,
    57056,
    55157,
    54413,
    60804,
    60834,
    57766
]
kuoerka = [
    108745,
    108650,
    108694,
    108727,
    108692,
    108671,
    108705,
    108695,
    108735,
    108681,
    108658,
    108600,
    108696,
    108687,
    108706,
    108697,
    108739,
    108722,
    108758,
    108723,
    108718,
    108693,
    108728,
    108683,
    108661,
    108744,
    108765,
    108712,
    108725,
    108653,
    108721,
    108766,
    108702,
    108787,
    108749,
    108757,
    108724,
    108740,
    108769,
    108793,
    108799,
    108812,
    108797,
    108682,
    108736,
    108773,
    108652,
    108716,
    108761,
    108628,
    108737,
    108754,
    108753,
    108730,
    108767,
    108825,
    108768,
    108772,
    108764,
    108794,
    108752,
    108748,
    108630,
    108785,
    108762,
    108798,
    108788,
    108719,
    108713,
    108731,
    108796,
    108784,
    108801,
    108802,
    108743,
    108750,
    110598,
    108760,
    108810,
    108814,
    108759,
    108805,
    108809,
    108783,
    108763,
    108813,
    108791,
    108775,
    108755,
    108811,
    108770,
    108707,
    108800,
    108720,
    108789,
    108732,
    108790,
    108804,
    108738,
    108774
]
juchi = [
    9009,
    411,
    50675,
    1967,
    53132,
    48889,
    50601,
    43630,
    45114,
    52547,
    52553,
    56697,
    2663,
    43892,
    43691,
    47307,
    43951,
    49203,
    1870,
    53809,
    50864,
    47029,
    49392,
    51829,
    45517,
    56311,
    44719,
    46618,
    57388,
    52769,
    54170,
    3881,
    47225,
    51026,
    44675,
    55574,
    1904,
    44469,
    2944,
    49514,
    47127,
    1533,
    51834,
    54803,
    49789,
    47743,
    51901,
    49328,
    61090,
    49880,
    52889,
    50551,
    57093,
    49791,
    57833,
    56778,
    52546,
    50171,
    55300,
    61097,
    46127,
    51847,
    53126,
    52257,
    61085,
    52322,
    54022,
    57952,
    56314,
    61080,
    46361,
    57884,
    53691,
    57813,
    52801,
    57919,
    51579,
    61107,
    61084,
    57957,
    54546,
    55310,
    58134,
    55530,
    562,
    55825,
    61082,
    61064,
    57400,
    61074,
    58098,
    58282,
    48892,
    58279,
    51169,
    61086,
    56041,
    61111,
    56765,
    52774
]
xisheng = [
    48185,
    56276,
    50041,
    2000,
    48257,
    49577,
    49539,
    50239,
    47043,
    53144,
    51322,
    53146,
    45461,
    44878,
    52722,
    54463,
    53518,
    53181,
    51578,
    58089,
    58105,
    49606,
    61210,
    55962,
    61200,
    56487,
    49320,
    4533,
    58209,
    49448,
    48191,
    48855,
    55912,
    52144,
    53348,
    44787,
    55694,
    52292,
    49333,
    57229,
    53359,
    52757,
    56518,
    61196,
    56393,
    46901,
    55268,
    61211,
    61166,
    53872,
    61214,
    51615,
    57429,
    61212,
    61190,
    103596,
    47218,
    53862,
    56170,
    56333,
    57471,
    53807,
    57993,
    61189,
    61204,
    45682,
    53557,
    57898,
    61172,
    61184,
    58035,
    58122,
    61217,
    61181,
    61194,
    61207,
    61215,
    61171,
    57202,
    61202,
    58421,
    58297,
    61183,
    61174,
    61176,
    61218,
    61167,
    61208,
    56759,
    61182,
    56746,
    61216,
    58272,
    61199,
    61205,
    61197,
    50686,
    58334,
    110634,
    61185
]
awp = [
    173,
    608,
    34692,
    46308,
    2225,
    50146,
    48173,
    102385,
    407,
    1943,
    2241,
    103549,
    302,
    1515,
    103347,
    1632,
    103566,
    799,
    103564,
    45783,
    2923,
    1880,
    2446,
    102319,
    1549,
    48185,
    234,
    2272,
    103344,
    5459,
    103346,
    43522,
    2230,
    1537,
    414,
    7070,
    103356,
    102283,
    43379,
    109829,
    10852,
    56276,
    49126,
    44040,
    43599,
    3793,
    61674,
    46375,
    61675,
    50041,
    10540,
    2000,
    48257,
    49577,
    3795,
    61676,
    47154,
    745,
    49539,
    50239,
    47043,
    1944,
    541,
    270,
    44446,
    48343,
    51890,
    108577,
    49281,
    43932,
    46722,
    48906,
    44830,
    45644,
    45598,
    1217,
    45592,
    44681,
    43816,
    37038,
    43809,
    45713,
    49470,
    44722,
    103352,
    102441,
    400,
    43848,
    43736,
    527,
    602,
    864,
    396,
    47628,
    43393,
    45651,
    296,
    1946,
    3107,
    869
]

# running(xiongdao_list)
# time.sleep(2)
# running(lieshazhebishou_list)
# running(chuangchang_list)
# running(anyingshuangbi)
# running(duanjian)
# running(kuoerka)
# running(juchi)
# running(xisheng)
# running(awp)




