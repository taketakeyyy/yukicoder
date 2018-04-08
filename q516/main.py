
if __name__ == "__main__":
    S1 = input()
    S2 = input()
    S3 = input()
    red  = 0
    if S1 == "RED":
        red += 1
    if S2 == "RED":
        red += 1
    if S3 == "RED":
        red += 1

    if red >= 2:
        print("RED")
    else:
        print("BLUE")
