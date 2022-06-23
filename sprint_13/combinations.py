def letter_comb(values):
    phone_key = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(values, pos, result):
        if values == '':
            result.append(pos)
            return
        for key in phone_key[values[0]]:
            pos += key
            backtrack(values[1:], pos, result)
            pos = pos[:-1]
    result = []
    backtrack(values, '', result)
    for i in result:
        print(i, end=' ')


numbers = input()
letter_comb(numbers)
