
if __name__ == "__main__":
    B = list(map(int, input().split()))
    for i in range(len(B)):
        if (i+1) != B[i]:
            print(i+1)
            exit()
    print(10)
