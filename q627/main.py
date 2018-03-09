#-*- coding:utf-8 -*-

if __name__ == "__main__":
    x = 0
    T = int(input())
    for i in range(T):
        next_x = int(input())
        if next_x == x+1:
            x = next_x
            continue
        elif next_x == x-1:
            x = next_x
            continue
        else:
            print("F")
            exit()
    print("T")
