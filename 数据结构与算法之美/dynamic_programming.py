#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""动态规划"""


class DynamicProgramming:

    # 0-1背包问题 items：物品重量 w：背包可承受重量
    def f(self, items, w):
        size = len(items)
        states = [[False for _ in range(w+1)] for _ in range(size)]
        states[0][0] = True
        states[0][items[0]] = True
        for i in range(1, size):
            for j in range(w+1):
                if states[i-1][j]:
                    states[i][j] = True
            for j in range(w+1-items[i]):
                if states[i-1][j]:
                    states[i][j+items[i]] = True
        for i in reversed(range(w+1)):
            if states[size-1][i]:
                return i
        return 0

    # 0-1背包问题空间优化 items：物品重量 w：背包可承受重量
    def f_opt(self, items, w):
        size = len(items)
        states = [False for _ in range(w+1)]
        states[0] = True
        states[items[0]] = True
        for i in range(1, size):
            for j in reversed(range(w+1-items[i])):
                if states[j]:
                    states[j+items[i]] = True
        for i in reversed(range(w+1)):
            if states[i]:
                return i
        return 0

    # 0-1背包问题，求最大价值 values：每个物品的价值
    def f_max_value(self, items, values, w):
        size = len(items)
        value_states = [-1 for _ in range(w+1)]
        value_states[0] = 0
        value_states[items[0]] = values[0]
        for i in range(1, size):
            for j in reversed(range(w + 1 - items[i])):
                if value_states[j] >= 0:
                    v = value_states[j] + values[i]
                    if v > value_states[j+items[i]]:
                        value_states[j+items[i]] = v
        max_value = -1
        for i in range(w+1):
            if value_states[i] > max_value:
                max_value = value_states[i]
        return max_value

    # 求出杨辉三角的最短路径
    def find_min_sums(self, yh_triangle):
        size = len(yh_triangle)
        min_sums = [0 for _ in range(size)]
        min_sums[0] = yh_triangle[0][0]
        for i in range(1, size):
            for j in reversed(range(i+1)):
                if j == 0:
                    min_sums[j] = min_sums[j] + yh_triangle[i][j]
                elif j == i:
                    min_sums[j] = min_sums[i-1] + yh_triangle[i][j]
                else:
                    min_sums[j] = min(min_sums[j-1], min_sums[j]) + yh_triangle[i][j]
        min_sum = min_sums[0]
        for i in min_sums:
            if i < min_sum:
                min_sum = i
        return min_sum

    # 硬币找零问题 coin_list:已有的硬币价格 price:总价
    def find_min_coins(self, coin_list, price):
        min_nums = [0 for _ in range(price + 1)]
        for i in coin_list:
            min_nums[i] = 1
        while True:
            for i in reversed(range(price + 1)):
                for j in reversed(coin_list):
                    if min_nums[price] > 0:
                        return min_nums[price]
                    if min_nums[i] > 0 and i + j <= price:
                        min_nums[i + j] = 1 + min_nums[i]

    # 求一个序列中的最长递增子序列长度
    def find_sub_max_length(self, test_list):
        size = len(test_list)
        max_length_list = [1 for _ in range(size)]
        for i in range(1, size):
            for j in reversed(range(0, i)):
                # 小于test_list[i]的最长子序列长度
                max_i_length = 1
                if test_list[i] > test_list[j]:
                    max_i_length = 1 + max_length_list[j]
                    break
            max_length_list[i] = max(max_length_list[i-1], max_i_length)
        return max_length_list[size - 1]


if __name__ == '__main__':
    # items = [2, 2, 4, 6, 3]
    # values = [3, 4, 8, 9, 6]
    # w = 9
    # print(DynamicProgramming().f_max_value(items, values, w))
    # yh_triangle = [[5], [7, 8], [2, 3, 4], [4, 9, 6, 1], [2, 7, 9, 4, 5]]
    # print(DynamicProgramming().find_min_sums(yh_triangle))
    # print(DynamicProgramming().find_min_coins([1, 3, 5], 10))
    test_list = [2, 9, 3, 6, 5, 1, 7]
    print(DynamicProgramming().find_sub_max_length(test_list))
