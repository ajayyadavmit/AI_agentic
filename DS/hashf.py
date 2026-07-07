

frutis = {
    "apple": 55,
    "orange": "Sindhuli",
    "papaya": "kathamndu"
}

for k,v in frutis.items():
    print(k, hash(k), ">>>😂 >>", v)


print(hash(-2))

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_iterative(44))  # 55

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_recursive(7))  # 55


def find_min_max_naive(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

print(find_min_max_naive([44,4,2,88]))
import numpy as np 

a= np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
print(type(a), a*b)

print(hash(11**1000))

print([ [ 0 for x in range(5)] for x in range(5)])
print(len([ [ 0 for x in range(5)] for x in range(5)]))

print(np.array([ [ 0 for x in range(5)] for x in range(5)]))
a = np.array([ [ 3 for x in range(5)] for x in range(5)])
print(a.ndim)
b = np.array([ [ 2 for x in range(5)] for x in range(5)])
print(a*b, a-b)