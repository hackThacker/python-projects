# write a program to find largest elemen in array

def larg(arr):
    if not arr:
        return ("Array is empty")

    large = arr[0]

    for element in arr:
        if element > large:
            large = element

    return large
        
array = [10, 20, 30, 40, 50]
result = larg(array)
print(f"The largest element in this {array} is :{result}")

