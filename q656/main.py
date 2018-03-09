#-*- coding:utf-8 -*-

if __name__ == "__main__":
    S = input()
    ans = 0
    for c in S:
        n = int(c)
        if n == 0:
            ans += 10
            continue
        ans += n
    print(ans)
