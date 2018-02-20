if __name__ == "__main__":
  N = int(input())
  for i in range(N,0,-1):
    s = ""
    for j in range(i): s += str(N)
    print(s)