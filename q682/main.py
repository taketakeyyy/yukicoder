import math

if __name__ == "__main__":
    A, B = list(map(int, input().split()))
    count = 0
    # Aから初めて3で割り切れるものを探す
    for i in range(A, B+1):
        if (A+i+B)%3 == 0:
            count += 1
            break
    # 初めて3で割り切れるもの以降は、O(1)で計算できる
    count += math.floor((B-i)/3)
    print(count)
