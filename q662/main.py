# -*- coding:utf-8 -*-

if __name__ == "__main__":
    strs = {}
    for i in range(5):
        str_, coin = input().split()
        strs[str_] = int(coin)
    n1 = int(input())
    A = [input() for i in range(n1)]
    n2 = int(input())
    B = [input() for i in range(n2)]
    n3 = int(input())
    C = [input() for i in range(n3)]
    # 期待値計算
    U = {}
    all_ways = n1*n2*n3
    kitai = 0
    for egara in strs:
        U[egara] = A.count(egara) * B.count(egara) * C.count(egara) * 5
        kitai += (U[egara] / all_ways) * strs[egara]
    # 出力
    print(kitai)
    for egara in U:
        print(U[egara])
