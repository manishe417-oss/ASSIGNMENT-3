n=int(input("Enter a number:"))
def fn(n):
    if n < 2 :
        return 1
    else:
        return n * (fn(n-1))

a=fn(n)
print(a)
