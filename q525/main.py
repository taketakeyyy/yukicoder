
if __name__ == "__main__":
    hh, mm = input().split(":")
    iHour = int(hh)
    iMin  = int(mm) + 5
    if iMin >= 60:
        iMin -= 60
        iHour += 1
    if iHour >= 24:
        iHour -= 24
    print("{0:02d}:{1:02d}".format(iHour, iMin))
