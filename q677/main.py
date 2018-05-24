
if __name__ == "__main__":
    N = int(input())
    a = 10**N
    if a == 1:
        print(1)
        exit()

    # 2のi乗を集める
    list_2 = []
    for i in range(0, N+1):
        list_2.append(2**i)

    ans = []
    for i in range(N+1):
        for j in list_2:
            ans.append(j * (5**i))
    ans.sort()

    # 出力
    for i in ans:
        print(i)
