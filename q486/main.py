
if __name__ == "__main__":
    S = input()
    east = 0
    west = 0
    for i in range(len(S)):
        if S[i] == "O":
            east += 1
            west = 0
        else:
            east = 0
            west += 1
        if east >= 3:
            print("East")
            exit()
        elif west >= 3:
            print("West")
            exit()
    print("NA")
