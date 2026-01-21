def prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return "composite"
    return "Prime"

n = int(input())
if n >= 2:
    print(prime(n))
else:
    print("number less than 2")