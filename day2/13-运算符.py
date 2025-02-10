# 刘飞鸿
# 2025年02月05日
# 1742357399@qq.com


def use_sum():
    '''
    算数运算
    :return:
    '''
    a = 5 / 2
    print(a)
    a = 5 // 2
    print(a)


def use_compare():
    print(3 > 5)


def use_logic():
    '''
    使用逻辑
    :return:
    '''
    print(1 and 4)  # 若都真，则返回后一个 短路运算
    print(0 or -1)  # 若都假，则返回前一个


def use_bit():
    '''
    位运算
    :return:
    '''
    print(5 & 7)  # 按位与
    print(5 | 7)  # 按位或
    print(~5)  # 按位取反
    print(5 ^ 7)  # 按位异或
    print(5 << 2)  # 左移永远乘2

    print(520 >> 2)  # 低位丢弃，正数右移永远除2 负数右移减1除2
    print(-5 >> 1)
    # 异或特点 与0异或不变 与自身异或变0
    print(5 ^ 5)
    print(5 ^ 0)


use_sum()
use_compare()
use_logic()
use_bit()
