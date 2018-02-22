# -*- coding: utf-8 -*-
if __name__ == "__main__":
	N = int(input())
	X = 1
	"""
	[方針]
	  Nを「2で割り切れるなら除算する」or「1を加算」していき、Nが1になったら終了
	"""
	cnt = 0
	while 1:
		if N == 1:
			break
		if N%2 == 0:
			N = N/2
			cnt += 1
		else:
			N += 1
			cnt += 1
	print(str(cnt))
