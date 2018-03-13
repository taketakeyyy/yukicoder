#-*- coding:utf-8 -*-

if __name__ == "__main__":
    P1 = int(input())
    P2 = int(input())
    N  = int(input())
    rooms = {}
    lost_money = 0
    for i in range(N):
        rsv = input()
        if rsv in rooms:
            lost_money += P1 + P2
        else:
            rooms[rsv] = 1
    print(lost_money)
