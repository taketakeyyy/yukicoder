import math

if __name__ == "__main__":
    L, K = list(map(int, input().split()))
    if L%(2*K) == 0:
        count = math.floor(L/(2*K))
        if count >= 1:
            count = count - 1
        else:
            count = 0
    else:
        count = math.floor(L/(2*K))
    print(count * K)
