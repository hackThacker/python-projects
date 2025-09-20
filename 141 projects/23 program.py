# write a program to find HCF 

def hcf(x,y):

#chose smaller value
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
            if ((x % i == 0)and (y % i == 0)):
                hcf = i
    return hcf

x1 = int(input("enter the value of x  : "))
y1 = int (input("Enter the value of y : "))

print(" the hcf is ", hcf(x1, y1))
