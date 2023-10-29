# Условия задачи:
# https://contest.yandex.ru/contest/44070/problems/B/
from collections import Counter


def count_points(matrix: str, k: int) -> int:
    nums_dict = Counter(matrix)
    point_counter = sum(num <= k*2 for num in nums_dict.values())
    return point_counter


def read_input() -> str:
    k = int(input())
    matrix = ''.join([input().replace('.', '') for _ in range(4)])
    return matrix, k


def sleight_of_hand() -> int:
    matrix, k = read_input()
    print(count_points(matrix, k))


if __name__ == '__main__':
    sleight_of_hand()
