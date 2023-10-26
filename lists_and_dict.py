#  1. Исходный список содержит положительные и отрицательные числа.
# Необходимо положительные поместить в один список,
# а отрицательные – в другой, затем отсортировать оба списка.
#  2. На основе первого списка, сформированного в
# предыдущей задаче, создайте множество чисел, противоположные
# к которым присутствуют в другом списке.
# Создайте словарь, ключами которого
# будут элементы множества в строковом представлении, а значениями — сами
# элементы множества.

nums = [3, -1, 5, -2, 7, -4, 0, 8, -6, 2, -3, -8]


def get_two_list(nums: list):
    positive_nums = []
    negative_nums = []
    for num in nums:
        if num > 0:
            positive_nums.append(num)
        elif num < 0:
            negative_nums.append(num)
    positive_nums.sort()
    negative_nums.sort()
    return positive_nums, negative_nums


def get_opposite_nums(positive_nums, negative_nums):
    opposite_nums = set()
    for num in positive_nums:
        if (0-num) in negative_nums:
            opposite_nums.add(num)
    dictionary_nums = {}
    for num in opposite_nums:
        dictionary_nums[str(num)] = num
    return dictionary_nums


def main():
    positive_nums, negative_nums = get_two_list(nums)
    dictionary_nums = get_opposite_nums(positive_nums, negative_nums)
    print(f'Положительные числа: " {positive_nums}',
          f'Отрицательные числа: " {negative_nums}',
          f'Словарь со значениями и ключами в строковом представлении: '
          f'{dictionary_nums}', sep='\n')


main()
