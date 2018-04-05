
if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))
    ans = {}
    # 回答する
    ans[L[0]] = 1
    max_key = L[0]
    max_val = 1
    for i in range(1, len(L)):
        if L[i] in ans:
            ans[L[i]] += 1
            if ans[L[i]] > max_val:
                max_key = L[i]
                max_val = ans[L[i]]
        else:
            ans[L[i]] = 1
        if ans[L[i]] == max_val:
            if L[i] > max_key:
                max_key = L[i]
                max_val = ans[L[i]]
    print(max_key)
