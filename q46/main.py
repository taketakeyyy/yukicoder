#-*- coding:utf-8 -*-
import math
if __name__ == "__main__":
	a, b = list(map(int, input().split(" ")))
	# try solving: ax >= b
	print(math.ceil(b/a))
