# -*- coding:utf-8 -*-

if __name__ == "__main__":
    COUNT = int(input())
    for i in range(COUNT):
        N = int(input())
        if N%8 == 0 and N%10 == 0:
            print("ikisugi")
            continue
        elif N%8 == 0:
            print("iki")
            continue
        elif N%10 == 0:
            print("sugi")
            continue
        print(int(N/3))
