"""
@Author  : liuyang
@Time    : 2023/4/17 15:26
@Content : 
"""

class Buff_config:

    #商品id,886606=梦魇,
    goods_id = 886606

    url = "https://buff.163.com/api/market/goods/sell_order?allow_tradable_cooldown=1&appid=730&goods_id="+str(goods_id)+"&page_num=1&page_size=24"
    payload={}
    headers = {
      'Host': 'buff.163.com',
      'Cookie': 'csrf_token=IjM5YTI2ZGJjM2UxMjM1MDllM2I0ZDc2OTdkYmVlNDFlN2I2YTEwNzIi.Fx6Ekg.PYu0vuvMMZqm8k1Y6ye4tTtoZGY; session=1-2lbrUeYzK-2BJqpBY_U5E_SJum3_yNbH4sHOOvt0xVOD2035829403; Device-Id=8CE2D1A5-EC26-40ED-8D63-BFF76367B409; Device-Id-Weak=8CE2D1A5-EC26-40ED-8D63-BFF76367B409; Locale-Supported=zh-Hans; webview_app_version=2.64.0.0; webview_from=iOS; csrf_token=IjM5YTI2ZGJjM2UxMjM1MDllM2I0ZDc2OTdkYmVlNDFlN2I2YTEwNzIi.Fx6FLg.6gZgxkAVsCmGBddDHtHGRTKQzKg; session=1-2lbrUeYzK-2BJqpBY_U5E_SJum3_yNbH4sHOOvt0xVOD2035829403',
      'user-agent': 'buff_release/2.64.0 (iPhone; iOS 16.3; Scale/3.00)',
      'timezone-offset': '28800000',
      'devicename': 'iPhone',
      'device-id-weak': '8CE2D1A5-EC26-40ED-8D63-BFF76367B409',
      'screen-scale': '3',
      'resolution': '1179x2556',
      'locale': 'zh-Hans-CN',
      'device-token': '5f45ab86be35e544c72d592274661289436f7d3af7c231b0b27857564faa47d2',
      'system-version': '16.3',
      'device-id': '8CE2D1A5-EC26-40ED-8D63-BFF76367B409',
      'locale-supported': 'zh-Hans',
      'timestamp': '1681715987.311597',
      'accept-language': 'zh-Hans-CN;q=1',
      'timezone': 'Asia/Shanghai',
      'network': 'WIFI',
      'product': 'iPhone 14 Pro',
      'timezone-offset-dst': '28800000',
      'model': 'iPhone',
      'accept': 'application/json',
      'app-version': '2.64.0',
      'app-version-code': '2.64.0.0',
      'system-type': 'iOS'
    }



