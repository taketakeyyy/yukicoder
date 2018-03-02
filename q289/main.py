# -*- coding:utf-8 -*-

def _int_or_false(c):
	try:
		return int(c)
	except:
		return False


if __name__ == "__main__":
	S = input()
	ans = 0
	for c in S:
		n = _int_or_false(c)
		if n is False: continue
		ans += n
	print(ans)
