def gen_bracket(index, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            gen_bracket(index + 1, n1 - 1, n2, prefix + '(')
        if index > 0 and n2 > 0:
            gen_bracket(index - 1, n1, n2 - 1, prefix + ')')


n = int(input())
n1 = n
n2 = n
index = 0
gen_bracket(index, n1, n2, '')
