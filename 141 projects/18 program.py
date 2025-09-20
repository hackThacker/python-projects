# write a program to print the fibonacci sequence

nterms = int(input(" how many terms : "))
 
# first two terms
n1, n2 = 0, 1
count = 0

#check the terms is valid 
if nterms <= 0:
    print("Enter the positive number")
elif nterms == 1:
    print("fibonance sequence upto ",nterms,":")
    print(n1)
else:
    print("fibonacci sequence")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        #update values
        n1 = n2 
        n2 = nth
        count += 1
