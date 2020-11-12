a = int(input())
b = int(input())
c = int(input())
if (a == b | a == c | b == c):
    print(0)
else:
    if (a < b):
        if (b < c):
            max = c
            mid = b
            min = a
        elif (a < c):
            max = b
            mid = c
            min = a
        else:
            max = b
            mid = a
            min = c
    else:
        if (c < b):
            max = a
            mid = b
            min = c
        elif (a < c):
            max = c
            mid = a
            min = b
        else:
            max = a
            mid = c
            min = b
    if ((max - mid) == (mid - min)):
        print(1)
    else:
        print(0)

