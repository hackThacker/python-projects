#write a pogram to find LCM

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

x1 = int(input("Enter the value of x: "))
y1 = int(input("Enter the value of y: "))

print("The LCM is", lcm(x1, y1))
