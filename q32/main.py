#-*- coding:utf-8 -*-
import math

if __name__ == "__main__":
	K = 0             # 1000
	L = int(input())  # 100
	M = int(input())  # 25
	N = int(input())  # 1

	ex_M = math.floor(N/25)
	N -= ex_M*25

	M += ex_M
	ex_L = math.floor(M/4)
	M -= ex_L*4

	L += ex_L
	ex_K = math.floor(L/10)
	L -= ex_K*10

	K += ex_K

	print(N+M+L)
