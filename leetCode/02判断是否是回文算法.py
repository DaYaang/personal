# 对输入的数字进行判断是否是回文（从左到右和从右到左一致），如123不是，131是
def num_check(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    else:
        return False

print(num_check(121))
print(num_check(12113))