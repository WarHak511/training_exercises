#  Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить,
# имеет длину n, то есть состоит из n одинаковых идущих подряд участков.
# Каждый участок либо пустой, либо на нём уже построен дом.
#
#  Общительный Тимофей не хочет жить далеко от других людей на этой улице.
# Поэтому ему важно для каждого участка знать
# расстояние до ближайшего пустого участка.
# Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.
#
#  Помогите Тимофею посчитать искомые расстояния.
# Для этого у вас есть карта улицы.
# Дома в городе Тимофея нумеровались в том порядке, в котором строились,
# поэтому их номера на карте никак не упорядочены.
# Пустые участки обозначены нулями.


def find_closest_zero(street_len, lots):

    left_zero_idx: int = lots.index('0')
    dist_to_zero: list[int] = [0] * street_len

    for i in range(street_len):
        if lots[i] == '0':
            left_zero_idx = i
        else:
            diff: int = abs(i - left_zero_idx)
            dist_to_zero[i] = diff

    if lots.count('0') > 1:
        right_zero_idx: int = street_len - lots[::-1].index('0') - 1
        for i in reversed(range(street_len)):
            if dist_to_zero[i] == 0:
                right_zero_idx = i
            else:
                diff: int = abs(i - right_zero_idx)
                if diff < dist_to_zero[i]:
                    dist_to_zero[i] = diff
    return dist_to_zero


def read_input():
    street_len = int(input())
    lots = input().split()
    return street_len, lots


def closest_zero():
    street_len, lots = read_input()
    print(*find_closest_zero(street_len, lots))


if __name__ == '__main__':
    closest_zero()
