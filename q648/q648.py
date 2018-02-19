# -*- coding: utf-8 -*-
import math
from decimal import *

def simple(n, N):
	""" TLEします """
	sum_sheep = 0
	for i in range(1,N+1):
		sum_sheep += i
		if sum_sheep < n:
			continue
		elif sum_sheep == n:
			print("YES")
			print(i)
			exit()
		else:
			print("NO")
			exit()

def sum_one_to_n(n, N):
	""" 1からnまでの和 = n*(n+1)/2 を求める
	veryverylarge1.txtでTLE
	"""
	for i in range(1, N+1):
		sum_sheep = i*(i+1)/2
		if sum_sheep < n:
			continue
		elif sum_sheep == n:
			print("YES")
			print(i)
			exit()
		else:
			print("NO")
			exit()

def _formula(n):
	""" 2次方程式の解
	99_corner3.txtでWAになる（桁落ちが原因）
	"""
	D = 1 + 8*n
	return (-1 + math.sqrt(D))/2  # ※式

def _formula2(n):
	""" 2次方程式の解
	桁落ちに対処するため、quadratic_formulaの※式を分子の有理化したもの
	Decimalで有効数字の精度を上げないと、99_corner6.txtでWAになる
	"""
	D = 1 + 8*n
	return Decimal(4*n)/Decimal(1+math.sqrt(D))

def quadratic_formula(n):
	""" ２次方程式の解を求める方法
	1からnまでの和の公式を変形すると、
	i**2 + i - 2*n = 0
	このときのiを求めて、iが正の整数ならば"YES"である
	"""
	i = _formula2(n)
	if i != math.floor(i):
		print("NO")
		exit()
	print("YES")
	print(int(i))
	exit()

if __name__ == "__main__":
	n = int(input())
	N = 2*(10**18)
	getcontext().prec = 24
	quadratic_formula(n)
