#-*- coding:utf-8 -*-

if __name__ == "__main__":
    heights = {}
    heights[int(input())] = "A"
    heights[int(input())] = "B"
    heights[int(input())] = "C"

    for h in sorted(heights.keys(), key=lambda x: -x ):
        print(heights[h])
