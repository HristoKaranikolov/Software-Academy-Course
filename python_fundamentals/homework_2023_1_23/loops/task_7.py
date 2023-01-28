# Create a program, that prints Fibonacci numbers from 0 to 50.

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


result = []
counter = 0
while True:
    func_res = recur_fibo(counter)
    if func_res > 50:
        break
    result.append(func_res)
    counter += 1

print(result)