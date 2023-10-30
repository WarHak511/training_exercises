# условия задачи https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num

    return -1
