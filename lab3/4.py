def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))

private_key_alice = int(input("Enter Alice's private key: "))
private_key_bob = int(input("Enter Bob's private key: "))

public_key_alice = mod_exp(g, private_key_alice, p)
public_key_bob = mod_exp(g, private_key_bob, p)

shared_secret_alice = mod_exp(public_key_bob, private_key_alice, p)
shared_secret_bob = mod_exp(public_key_alice, private_key_bob, p)

print(f"Public Key of Alice: {public_key_alice}")
print(f"Public Key of Bob: {public_key_bob}")

if shared_secret_alice == shared_secret_bob:
    print(f"Shared Secret Key: {shared_secret_alice}")
    print("Key Excha1nge Successful!")
else:
    print("Key Exchange Failed!")
