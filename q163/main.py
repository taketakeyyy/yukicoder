#-*- coding:utf-8 -*-

if __name__ == "__main__":
	S = input()
	ans = ""
	for c in S:
		if ord(c) >= 97:
			# cは小文字 A...Z
			ans += c.upper()
		else:
			# cは大文字文字 a...z
			ans += c.lower()
	print(ans)
