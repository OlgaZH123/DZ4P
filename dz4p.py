# Задача 22
# numbers_1 = sorted(set(input('Введите первую последовательность: ').split()))
# print(numbers_1)

# numbers_2 = sorted(set(input('Введите вторую последовательность: ').split()))
# print(numbers_2)

# result = [int(i) for i in numbers_1 if i in numbers_2]
# result = [int(i) for i in numbers_1 if i in numbers_2]
# print(*sorted(result))

# Задача 24
import random


def get_garden_bed(n):
    garden_bed = [random.randint(10, 30) for _ in range(n)]  
    garden_bed=[1,2,3,4]
    print(garden_bed)
    return garden_bed


def get_berries(garden_bed):
    if len(garden_bed) < 3:
        print(sum(garden_bed))
    else:
        result = []
        garden_bed += garden_bed[:2]  
        print(garden_bed)
        [result.append(sum(garden_bed[i - 1:i + 2])) for i in range(len(garden_bed))]
        print(result)
        print(max(result))


def main():
    n = int(input('Введите количество кустов: '))
    garden_bed = get_garden_bed(n)
    get_berries(garden_bed)


if __name__ == '__main__':
    main()