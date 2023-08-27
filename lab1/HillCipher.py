import numpy as np

def pad_plaintext(plaintext, block_size):
    # Pad the plaintext with 'X' to make its length a multiple of block_size
    padding_size = (block_size - len(plaintext) % block_size) % block_size
    return plaintext + 'X' * padding_size

def encrypt_block(block, key_matrix):
    # Convert block to a column vector
    block_vector = np.array([ord(char) - ord('A') for char in block])
    
    # Perform matrix multiplication with the key matrix
    encrypted_vector = np.dot(key_matrix, block_vector) % 26

    # Convert the encrypted vector back to a string
    encrypted_block = ''.join([chr(num + ord('A')) for num in encrypted_vector])
    return encrypted_block

def hill_cipher_encrypt(plaintext, key_matrix):
    block_size = key_matrix.shape[0]
    plaintext = pad_plaintext(plaintext.upper(), block_size)
    encrypted_text = ""

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        encrypted_block = encrypt_block(block, key_matrix)
        encrypted_text += encrypted_block

    return encrypted_text

# Example usage:
plaintext = "Rohit"
key_matrix = np.array([[6, 24], [13, 16]])  # 2x2 key matrix

encrypted_text = hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:", encrypted_text)


# import numpy as np
# def matrix_mod_inv(matrix, modulus):
#     """We find the matrix modulus inverse by
#     Step 1) Find determinant
#     Step 2) Find determinant value in a specific modulus (usually length of alphabet)
#     Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
#     """
#     det = int(np.round(np.linalg.det(matrix)))  # Step 1)
#     det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
#     matrix_modulus_inv = (
#         det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
#     )  
#     return matrix_modulus_inv
# def encrypt(message, K):
#     encrypted = ""
#     message_in_numbers = []

#     for letter in message:
#         message_in_numbers.append(letter_to_index[letter])

#     split_P = [
#         message_in_numbers[i : i + int(K.shape[0])]
#         for i in range(0, len(message_in_numbers), int(K.shape[0]))
#     ]
#     for P in split_P:
#         P = np.transpose(np.asarray(P))[:, np.newaxis]

#         while P.shape[0] != K.shape[0]:
#             P = np.append(P, letter_to_index[" "])[:, np.newaxis]

#         numbers = np.dot(K, P) % len(alphabet)
#         n = numbers.shape[0]  
#         for idx in range(n):
#             number = int(numbers[idx, 0])
#             encrypted += index_to_letter[number]

#     return encrypted

# def main():
#     message = input("enter a plain text to encrypt")

#     K = np.matrix([[3, 3], [2, 5]])
#     Kinv = matrix_mod_inv(K, len(alphabet))

#     encrypted_message = encrypt(message, K)
#     print("Original message: " + message)
#     print("Encrypted message: " + encrypted_message)
# main()
    