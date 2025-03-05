"""
@Author  : liuyang
@Time    : 2023/1/10 11:34
@Content : yunding_admin 添加数据库数据
"""

import pymysql
import time

# 数据库连接
db_yunding_admin = pymysql.connect(host="47.113.36.113", user="root", password="pT1U8h55JbEWy6MAc3jK",
                                   database="yunding_admin")
# 创建游标
cursor = db_yunding_admin.cursor()

inviter_account_id_list = [
    202301101729699,
    202301101835155,
    202301102051248,
    202301101931717,
    202301101613918,
    202301101267837,
    202301101582568,
    202301102085734,
    202301101850652,
    202301101303035,
    202301101633703,
    202301101454311,
    202301101802887,
    202301101711847,
    202301101258997,
    202301102008127,
    202301101443813,
    202301102020310,
    202301101511272,
    202301101666003,
    202301101700770,
    202301101492426,
    202301101377560,
    202301102005919,
    202301101753088,
    202301101325534,
    202301101684262,
    202301101445360,
    202301102049017,
    202301101878241,
    202301102061128,
    202301101846186,
    202301101249336,
    202301101895612,
    202301101483864,
    202301101888715,
    202301102120948,
    202301092263283
]

for i in range(0, len(inviter_account_id_list) + 1):

    times = "2023-01-10 15:00:00"
    inviter_account_id = inviter_account_id_list[i]
    nums = len(inviter_account_id_list)
    num1 = i + 100
    num2 = i + 50
    num3 = num2 * 1000
    # type =1 注册 num 注册人数
    sql1 = f"INSERT INTO `yunding_admin`.`t_user_statis_day_data`(`statis_date`,\
   `union_id`, `num`, `type`, `inviter_account_id`, `op_platform`, `create_time`, `update_time`) \
   VALUES ( '{times}', 8, {num1}, 1, {inviter_account_id}, 'Android', '{times}', '{times}');"

    # type = 2 活跃，num 活跃人数
    sql2 = f"INSERT INTO `yunding_admin`.`t_user_statis_day_data`(`statis_date`,\
   `union_id`, `num`, `type`, `inviter_account_id`, `op_platform`, `create_time`, `update_time`) \
   VALUES ( '{times}', 8, {num1}, 2, {inviter_account_id}, 'Android', '{times}', '{times}');"

    # type = 3 充值人数，num 人数
    sql3 = f"INSERT INTO `yunding_admin`.`t_user_statis_day_data`(`statis_date`,\
   `union_id`, `num`, `type`, `inviter_account_id`, `op_platform`, `create_time`, `update_time`) \
   VALUES ( '{times}', 8, {num2}, 3, {inviter_account_id}, 'Android', '{times}', '{times}');"

    # type = 4 充值金额(元)，num 金额
    sql4 = f"INSERT INTO `yunding_admin`.`t_user_statis_day_data`(`statis_date`,\
   `union_id`, `num`, `type`, `inviter_account_id`, `op_platform`, `create_time`, `update_time`) \
   VALUES ( '{times}', 8, {num3}, 4, {inviter_account_id}, 'Android', '{times}', '{times}');"

    try:
        cursor.execute(sql2)
        cursor.execute(sql2)
        cursor.execute(sql3)
        cursor.execute(sql4)
        db_yunding_admin.commit()
        print(f"{inviter_account_id_list[i]}增加已执行成功")
    except:
        db_yunding_admin.rollback()

# 关闭数据
db_yunding_admin.close()
