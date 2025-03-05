"""
@Author  : liuyang
@Time    : 2023/10/25 13:35
@Content : 
"""
# -*- coding: UTF-8 -*-
"""
# ---------------------------------------
# @DateTime : 2022/12/5 8:11 PM
# @Author   : youpin
# @Email    :
# PyCharm
# @Description : 生成rsa2加密后的sign值
# ---------------------------------------
"""
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


class RsaUtils(object):

    def __init__(self, private_key):
        self.private_key = private_key



    def b64encode(self, bytes: bytes) -> bytes:
        '''
        base64 encode
        :param bytes:
        :return: str
        '''
        return base64.b64encode(bytes)

    def b64decode(self, paivate_key: str) -> bytes:
        '''
        将私钥base64 decode
        :param paivate_key:
        :return:
        '''
        return base64.b64decode(paivate_key)

    def ordered_data_params(self, data) -> str:
        '''
        将请求的入参 dumps
        :param data: 请求的入参
        :return: 排序后的入参
        '''
        params = ""
        for key in sorted(data):
            value = json.dumps(data[key],separators=(',', ':'))
            if value:
                params += f"{key}{value}"
        return params

    def encrypt(self, string: str) -> str:
        '''
        rsa2 生成验签 sign
        :return:
        '''
        private_keyBytes = self.b64decode(self.private_key)
        priKey = RSA.importKey(private_keyBytes)
        signer = PKCS1_v1_5.new(priKey)
        hash_obj = SHA256.new(bytearray(string, encoding='utf-8'))
        signature = self.b64encode(signer.sign(hash_obj))
        return signature.decode()


if __name__ == '__main__':
    # 生成验签流程
    # 1.实例化类 并填入自己私钥
    # 2.准备自己的字典入参
    # 3.字典排序并生成加密前字符串
    # 4.生成sign

    private_key = "私钥"

    # 实例化类并填入自己私钥
    utils = RsaUtils(private_key=private_key)
    # 准备自己字典入参
    data = {
        "timestamp": "2023-12-05 16:15:00",
        "appKey": "123456",
        "idempotentId": "202212050001",
        "purchasingInfoList": [
            {
                "commodityId": 28347880,
                "commodityPrice": 0.12,
                "tradeLinks": "https://steamcommunity.com/tradeoffer/new/?partner=12345678912&token=LBPW679"
            },
            {
                "commodityId": 28347887,
                "commodityPrice": 0.12,
                "tradeLinks": "https://steamcommunity.com/tradeoffer/new/?partner=12345678912&token=LBPW679"
            },
            {
                "commodityId": 28347875,
                "commodityPrice": 0.12,
                "tradeLinks": "https://steamcommunity.com/tradeoffer/new/?partner=12345678912&token=LBPW679"
            }
        ]
    }

    # 字典排序
    params = utils.ordered_data_params(data)
    sign = utils.encrypt(string=params)
    print("sign:",sign)
