
if __name__ == "__main__":
    S = input()
    left = len(S.split("(^^*)")) - 1
    right = len(S.split("(*^^)")) - 1
    print("{} {}".format(left, right))
