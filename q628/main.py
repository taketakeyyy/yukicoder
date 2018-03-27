# -*- coding: utf-8 -*-


if __name__ == "__main__":
    N  = int(input())
    tag_dict = {}
    for i in range(N):
        No = int(input())
        M, S = list(map(int, input().split()))
        tags = input().split()
        for tag in tags:
            if tag in tag_dict:
                tag_dict[tag] += S
            else:
                tag_dict[tag] = S
    # 回答を出力する
    tag_items = list(tag_dict.items())
    tag_items.sort(key=lambda x: x[0])
    tag_items.sort(key=lambda x: x[1], reverse=True)
    item_len = len(tag_items)
    if item_len < 10:
        RANGE_MAX = item_len
    else:
        item_len = 10
    for i in range(item_len):
        print("{} {}".format(tag_items[i][0], tag_items[i][1]))
