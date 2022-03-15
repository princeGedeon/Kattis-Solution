def printerd(nb):
    printer=1
    days=0
    while printer<nb:
        printer=printer*2
        days+=1
    days+=1
    return days
print(printerd(int(input())))