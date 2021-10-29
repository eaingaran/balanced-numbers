import multiprocessing


def is_balanced(number, base):
    base_number = []
    while number != 0:
        base_number.insert(0, number % base)
        number = number // base
    if len(base_number) < 2:
        return True
    m = len(base_number) // 2
    if not len(base_number) % 2 == 0:
        m += 1
    l_num = base_number[:m]
    r_num = base_number[-m:]
    return sum(l_num) == sum(r_num)


def get_decimal(digits_list, digits_length, base):
    decimal_number = 0
    for index in range(1, digits_length + 1):
        decimal_number += digits_list[index-1] * pow(base, digits_length - index)
    return decimal_number


if __name__ == '__main__':
    B, L = [int(x) for x in input().split()]
    dL = [int(x) for x in input().split()]
    num = get_decimal(dL, L, B)
    balanced_numbers = []
    all_numbers = [(x, B) for x in range(1, num + 1)]
    with multiprocessing.Pool(processes=16) as pool:
        results = pool.starmap(is_balanced, all_numbers)
        for i in range(1, num + 1):
            if results[i-1]:
                balanced_numbers.append(i if i < 1004535809 else i % 1004535809)
    print(f'{len(balanced_numbers)} {sum(balanced_numbers) % 1004535809}')

