#-*- coding: utf-8 -*-
import math

def _exist_3(n):
	# 各位のいずれかに3がある？
	while 1:
		syou = math.floor(n/10)
		amari = n - syou*10
		if amari == 3:
			return True
		if syou == 0:
			return False
		n = syou

if __name__ == "__main__":
	A, B = list(map(int, input().split()))
	for i in range(A, B+1):
		if i%3 == 0 or _exist_3(i):
			print(i)
