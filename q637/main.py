# -*- coding: utf-8 -*-

if __name__ == "__main__":
    inputs = input().split()
    inputs = list(map(int, inputs))
    char_len = 0
    for a in inputs:
        if a%3==0 and a%5==0:
            char_len += 8
        elif a%3 == 0:
            char_len += 4
        elif a%5 == 0:
            char_len += 4
        else:
            char_len += len(str(a))
    print(char_len)
