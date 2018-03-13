#-*- coding:utf-8 -*-

if __name__ == "__main__":
    H, N = list(map(int, input().split()))
    ans = 1
    for i in range(N-1):
        if H < int(input()):
            ans += 1
    ans = str(ans)
    if ans[-1] == "1":
        print("{}st".format(ans))
    elif ans[-1] == "2":
        print("{}nd".format(ans))
    elif ans[-1] == "3":
        print("{}rd".format(ans))
    else:
        print("{}th".format(ans))
