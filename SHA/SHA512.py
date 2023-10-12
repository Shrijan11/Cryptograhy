def text_to_binary(input_text):
    binary_string = ''.join(format(ord(char), '08b') for char in input_text)
    return binary_string

# Get user input for the text to be hashed
input_text = input("Enter the text to be hashed: ")

input_binary = text_to_binary(input_text)

input_text = "TEST"

def text_to_binary(input_text):
    binary_string = ''.join(format(ord(char), '08b') for char in input_text)
    return binary_string

input_binary = text_to_binary(input_text)


def binary_padding(input_binary):
    # Calculate the length of the input binary (in bits)
    binary_length = len(input_binary)

    # Calculate the padding length so that the total length is a multiple of 1024 bits
    padding_length = 896 - (binary_length % 1024)

    # Create the padding
    padding = '1' + '0' * (padding_length - 1)

    # Convert the length of the binary to a 128-bit binary representation
    binary_length_128 = format(binary_length, '0128b')

    # Combine the input binary, padding, and length information
    result_binary = input_binary + padding + binary_length_128

    return result_binary

padded_binary = binary_padding(input_binary)

def divide_padded_message(padded_binary):
    words = []
    for i in range(0, len(padded_binary), 64):
        word = padded_binary[i:i+64]
        words.append(word)
    return words

padded_message = binary_padding(input_binary)
words = divide_padded_message(padded_message)

def expand_words(words):
    for i in range(16, 80):
        temp = int(words[i-3], 2) ^ int(words[i-8], 2) ^ int(words[i-14], 2) ^ int(words[i-16], 2)
        temp = ((temp << 1) | (temp >> 31)) & 0xFFFFFFFFFFFFFFFF  # Perform a 64-bit circular left shift
        words.append(format(temp, '064b'))
    return words


expanded_words = expand_words(words)

def sha512_processing(expanded_words, h_values):
    # Constants declaration
    K = [
        0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
        0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
        0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
        0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
        0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
        0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
        0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
        0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
        0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
        0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
        0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
        0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
        0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774df4df4d2f, 0x34b0bcb5e19b48a8,
        0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
        0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
        0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
        0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
        0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
        0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
        0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817,
    ]

    # Message schedule initialization
    message_schedule = expanded_words
    a, b, c, d, e, f, g, h = h_values

    for i in range(80):
        S1 = ((e >> 14) | (e << (64 - 14))) ^ ((e >> 18) | (e << (64 - 18))) ^ ((e >> 41) | (e << (64 - 41)))
        ch = (e & f) ^ ((~e) & g)
        temp1 = (h + S1 + ch + K[i] + int(message_schedule[i], 2)) & 0xFFFFFFFFFFFFFFFF

        S0 = ((a >> 28) | (a << (64 - 28))) ^ ((a >> 34) | (a << (64 - 34))) ^ ((a >> 39) | (a << (64 - 39)))
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (S0 + maj) & 0xFFFFFFFFFFFFFFFF

        h = g
        g = f
        f = e
        e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
        d = c
        c = b
        b = a
        a = (a + temp1) & 0xFFFFFFFFFFFFFFFF


    # Updating the hash values (h0 to h7)
    h_values[0] = (h_values[0] + a) & 0xFFFFFFFFFFFFFFFF
    h_values[1] = (h_values[1] + b) & 0xFFFFFFFFFFFFFFFF
    h_values[2] = (h_values[2] + c) & 0xFFFFFFFFFFFFFFFF
    h_values[3] = (h_values[3] + d) & 0xFFFFFFFFFFFFFFFF
    h_values[4] = (h_values[4] + e) & 0xFFFFFFFFFFFFFFFF
    h_values[5] = (h_values[5] + f) & 0xFFFFFFFFFFFFFFFF
    h_values[6] = (h_values[6] + g) & 0xFFFFFFFFFFFFFFFF
    h_values[7] = (h_values[7] + h) & 0xFFFFFFFFFFFFFFFF

# Returning the updated hash values
    return h_values


# Initializing h_values with the SHA-512 initial values
h_values = [
    0x6a09e667f3bcc908,
    0xbb67ae8584caa73b,
    0x3c6ef372fe94f82b,
    0xa54ff53a5f1d36f1,
    0x510e527fade682d1,
    0x9b05688c2b3e6c1f,
    0x1f83d9abfb41bd6b,
    0x5be0cd19137e2179
]

resulting_h_values = sha512_processing(expanded_words, h_values)

final_hash = ''.join(format(value, '016x') for value in resulting_h_values)

print(f"Final Hash: {final_hash}")