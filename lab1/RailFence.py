def rail_fence_encrypt(text, rails):
    rail_fence = [['' for _ in range(len(text))] for _ in range(rails)]
    direction = -1  # Downward initially
    row, col = 0, 0
    
    for char in text:
        rail_fence[row][col] = char
        if row == 0 or row == rails - 1:
            direction = -direction
        row += direction
        col += 1
    
    encrypted_text = ''.join(''.join(row) for row in rail_fence)
    return encrypted_text

def rail_fence_decrypt(encrypted_text, rails):
    rail_fence = [['' for _ in range(len(encrypted_text))] for _ in range(rails)]
    direction = -1  # Upward initially
    row, col = 0, 0
    
    for _ in range(len(encrypted_text)):
        rail_fence[row][col] = '*'
        if row == 0 or row == rails - 1:
            direction = -direction
        row += direction
        col += 1
    
    index = 0
    for row in rail_fence:
        for i in range(len(row)):
            if row[i] == '*':
                row[i] = encrypted_text[index]
                index += 1
    
    decrypted_text = ''
    row, col = 0, 0
    direction = -1  # Downward initially
    for _ in range(len(encrypted_text)):
        decrypted_text += rail_fence[row][col]
        if row == 0 or row == rails - 1:
            direction = -direction
        row += direction
        col += 1
    
    return decrypted_text

if __name__ == '__main__':
    text = "Rohit"
    rails = 3
    
    encrypted_text = rail_fence_encrypt(text, rails)
    print("Encrypted:", encrypted_text)
    
    decrypted_text = rail_fence_decrypt(encrypted_text, rails)
    print("Decrypted:", decrypted_text)
