for a in range(999, 0, -1):
    for x in range(1, 10 ** 5):
        if not(((x % a == 0) and (x % 37 == 0)) <= (x % 3737 == 0)):
            break
    else:
        print(a)
        break
