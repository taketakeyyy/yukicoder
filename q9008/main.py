#-*- coding:utf-8 -*-

if __name__ == "__main__":
	N = int(input())
	nums = list(map(int, input().split()))
	ans = 0
	for num in nums:
		ans += num
	print(ans)
