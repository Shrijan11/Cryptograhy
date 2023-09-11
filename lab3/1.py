import random

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False 

    return True  

if __name__ == "__main__":
    num = int(input("Enter a number to test for primality: "))
    k = int(input("Enter the number of iterations (default is 5): "))
    if miller_rabin(num, k):
        print(f"{num} is likely a prime number.")
    else:
        print(f"{num} is definitely a composite number.")
