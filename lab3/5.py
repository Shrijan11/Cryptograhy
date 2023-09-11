import random

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

while True:
    p = random.randint(100, 1000)
    if is_prime(p):
        break

while True:
    q = random.randint(100, 1000)
    if is_prime(q) and p != q:
        break

n = p * q
phi_n = (p - 1) * (q - 1)


while True:
    e = random.randint(2, phi_n - 1)
    if gcd(e, phi_n) == 1:
        break


d = mod_inverse(e, phi_n)


message = int(input("Enter a message to encrypt (as an integer): "))


encrypted_message = pow(message, e, n)


decrypted_message = pow(encrypted_message, d, n)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
