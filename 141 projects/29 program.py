#write a program to calculate the body mass index

def body(height, weight):
    return round((weight / height ** 2),2)

h = float(input("Enter your height in meter: "))
w = float(input("Enter your weight into kg : "))

bmi = body(h, w)
print("your Bmi is ", bmi)


if bmi <= 18.5:
    print("Your ar underweight")
elif 18.5 < bmi <= 24.9:
    print("your weight is normal")
elif 25 < bmi <= 29.20:
    print("your are overweight")
else:
    print("your are obese ")