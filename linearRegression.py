def squareN(n):
    a = []
    for i in range(n):
        b = input()
        a.append(int(b))
    for i in range(n):
        a[i] = pow(a[i],2)
        print(a[i],end =" ")
    return a
if __name__ == "__main__":
    n = input()
    n = int(n)
    array = squareN(n)
    pass
