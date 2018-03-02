#-*- coding:utf-8 -*-
import math

def _is_happyday(month, day):
	if month == _sum_digit(day):
		return True
	return False

def _sum_digit(n):
	d2 = math.floor(n/10)
	d1 = n - d2*10
	return d1 + d2

if __name__ == "__main__":
	count = 0
	calenders = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	for month in calenders:
		for i in range(1, calenders[month]+1):
			if _is_happyday(month, i):
				count += 1
	print(count)
