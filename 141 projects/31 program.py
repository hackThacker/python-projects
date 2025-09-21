# write a program for cube sum of first natural numbers

def cube(n):
    if n <= 0:
        return 0
    else:
        t = sum([i**3 for i in range(1, n + 1)])
        return t
    
n = int(input("enter the value of n :"))
if n <= 0:
    print("ente the positive number ")
else:
    result = cube(n)
    print(f"THe cuber sum fitst {n} natural numbe is : {result}")