def check_subsequence(string_s, string_t):
    subseq = 0
    result = False
    for letter in string_s:
        try:
            new_subseq = string_t.index(letter, subseq)
            subseq = new_subseq + 1
            result = True
        except ValueError:
            result = False
            break
    if len(string_s) == 0:
        result = True
    print(result)


string_s = input()
string_t = input()
check_subsequence(string_s, string_t)
