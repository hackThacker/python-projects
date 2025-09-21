# write a program to display  fibonacci sequence using recusion
def recu(n):
    if n <= 1:
        return n
    else:
        return(recu(n-1) + recu(n-2))
    
nterms = int(input("enter the number geter than 0"))

if nterms <= 0:
    print("enter the positive interger")
else:
    print("fibonanice sequence")
    for i in range(nterms):
        print(recu(i))