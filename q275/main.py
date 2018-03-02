#-*- coding:utf-8 -*-
import math

if __name__ == "__main__":
	N = int(input())
	nums = list(map(int, input().split()))
	nums.sort()
	if N%2 == 0:
		i = math.floor(N/2)
		print(round((nums[i-1]+nums[i])/2, 1))
	else:
		print(nums[int(N/2)])
