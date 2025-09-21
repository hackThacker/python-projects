# write a program to make the simple calculator

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        print("Cannot divide by zero!")
        return None

print("Select operation")
print("1. Add")
print("2. Sub")
print("3. Multiplication")
print("4. Divide")

while True:
    choice = input("Enter the choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first value: "))
            num2 = float(input("Enter the second value: "))
        except ValueError:
            print("Invalid value, please enter numbers.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {mult(num1, num2)}")

        elif choice == '4':
            result = div(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")

        again = input("Do you want to perform another calculation? (yes/no): ")
        if again in ("N","no", "nO", "NO", "No", "n"):
            break
    else:
        print("Please enter a valid choice.")
