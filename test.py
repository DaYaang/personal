"""
汇率查询
"""
from currency_converter import CurrencyConverter
from datetime import date
conv = CurrencyConverter()
c = conv.convert(1, 'CNY', 'HKD')
print(c,round(c, 2),type(round(c, 2)))
