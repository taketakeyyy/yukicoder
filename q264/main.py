#-*- coding:utf-8 -*-

if __name__ == "__main__":
	N, K = list(map(int, input().split()))
	#ぐー, ちょき, ぱーをそれぞれ 0, 1, 2
	result = N-K
	if result == -1 or result == 2:
		print("Won")
	elif result == 0:
		print("Drew")
	else:
		print("Lost")
