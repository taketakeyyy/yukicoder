
if __name__ == "__main__":
    S = input()
    if S[-2] == "a" and S[-1] == "i":
        print("{}{}{}".format(S[:-2], "A", "I"))
    else:
        print("{}-AI".format(S))
