"""
@Author  : liuyang
@Time    : 2023/4/17 15:24
@Content : 
"""
import jsonpath as jsonpath
import requests
from some_config import Buff_config

def query_box():

    url = Buff_config.url
    payload = Buff_config.payload
    headers = Buff_config.headers

    response = requests.request("GET", url, headers=headers, data=payload)

    # 取返回商品的所有价格
    res_json = response.json()
    all_price = jsonpath.jsonpath(res_json,'$.data.items..price')
    all_id =  jsonpath.jsonpath(res_json,'$.data.items..id')
    print("all_parice",all_price)

    gold_price_list = []
    # 取价格小于 12 的数据，返回对应下标：
    for price in all_price:
        if float(price) <= 13.4:
            gold_price_list.append(price)
    print("符合条件的价格：",gold_price_list)



    # 通过价格取对应id
    gold_id_list = []
    for gold_price in gold_price_list:
        pass




query_box()
