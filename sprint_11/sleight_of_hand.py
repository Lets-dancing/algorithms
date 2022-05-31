def sleight_of_hand():
    numbers = []
    scores = 0
    for symbol in range(1, 10):
        count = matrix.count(str(symbol))
        numbers.append(count)
    for symbol, value in enumerate(numbers):
        if value == 0:
            continue
        if int(value) <= num:
            scores += 1
    return scores


if __name__ == '__main__':
    num = int(input()) * 2
    matrix = ''
    matrix = ''.join([matrix + input() for symb in range(4)])
    print(sleight_of_hand())
