str1 = " ashdkash12i12asd卡卡加大好看12e23sjalk adjaskjdklq 1 1 123 2 "
str2 = "12345"
# 查找
print(str1.find("k"))
# 倒查
print(str1.rfind("k"))
# find找不到返回-1
print(str1.find("w",0,-1))
print(str1.index("k"))
print(str1.rindex("k"))
# index找不到会报错
print(str1.index("w"))

# 替换
print(str1.replace("a","X"))
print(str1.replace(" ",""))

# 分割
# 从左到右分割
print(str1.split("a"))
# 从右到左分割
print(str1.rsplit("a"))
str.split(sep=None, maxsplit=-1)
str.rsplit(sep=None, maxsplit=-1)
# 当maxsplit 为 -1 或分割次数足以将字符串完全分割时，split() 和 rsplit() 的结果相同。
# 当指定了有限的 maxsplit 值时，split() 从左向右分割，rsplit() 从右向左分割，这可能会导致不同的分割结果。

# 开头和结尾字符判断
print(str1.startswith("as"))
print(str1.endswith("a"))

# 去空格
# 去头尾
print(str1.strip())
# 只去头
print(str1.lstrip())
# 只去尾
print(str1.rstrip())

# 判断是否纯数字
print(str1.isalnum())
print(str2.isalnum())
