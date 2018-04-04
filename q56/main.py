import math

if __name__ == "__main__":
    D, P = list(map(int, input().split()))
    print(math.floor(D + (D * P / 100)))
