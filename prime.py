def prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Please enter a number: "))
if n >= 2:
    print(f"{n} is a {'Prime' if prime(n) else 'Composite'} number")
else:
    print("number less than 2, please enter a greater positive number")