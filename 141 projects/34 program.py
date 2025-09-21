# write a program for array rotation

def rotate(arr, d):
    n = len(arr)

    if d < 0 and d >= n:
        return "invalide rotation value"

    ro = [0] * n

    for i in range(n):
        ro[i] = arr[(i + d) % n]
    return ro

arr = [1, 2, 3, 4, 5]

d = 4

result = rotate(arr,d)

print(f"Orginal array : {arr} \nRotated Array : {result}")