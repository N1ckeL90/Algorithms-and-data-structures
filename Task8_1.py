# Определить количество различных подстрок с использованием хеш-функции. Задача: на вход
# функции дана строка, требуется вернуть количество различных подстрок в этой строке.
from hashlib import sha1


def count_substrings(s, t):
    len_sub = len(t)
    cnt = 0
    h_subs = sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        h = sha1(s[i:i+len_sub].encode('utf-8')).hexdigest()
        if h_subs == h:
            cnt += 1
    return cnt


def find_num_of_substrings(st):
    substrings = {}
    for pos in range(len(st)):
        for width in range(pos + 1, len(st)+1):
            subs = st[pos:width]
            if subs not in substrings.keys():
                c = count_substrings(st, subs)
                substrings[subs] = c
    return substrings


if __name__ == '__main__':
    _st = 'Задача'
    print(find_num_of_substrings(_st))
