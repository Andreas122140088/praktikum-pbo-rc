H=input("Height : ")
for i in range(1, int(H) + 1):
    print(" " * (int(H) - i) + "*" * (2 * i - 1))
