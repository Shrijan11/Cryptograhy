def shift(key, round):
    shiftByOne = [1, 2, 9, 16] 
    if(round in shiftByOne):
        key = key[1:] + key[0:1]
    else:
        key = key[2:] + key[0:2]
    return key

    
def main(key):
    leftSelection = [57, 49, 41, 33, 25, 17, 9,
                      1, 58, 50, 42, 34, 26, 18,
                     10, 2, 59, 51, 43, 35, 27,
                     19, 11, 3, 60, 52, 44, 36]

    rightSelection = [63,55, 47, 39, 31, 23, 15,
                       7,62, 54, 46, 38, 30, 22,
                      14,6, 61, 53, 45, 37, 29,
                      21,13, 5, 28, 20, 12, 4]
                    
    keySelection = [14, 17, 11, 24, 1, 5,   3, 28,
                    15, 6, 21, 10,  23, 19, 12, 4,
                    26, 8, 16, 7,   27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]
    
    keys = ["" for i in range(16)]
    left = ""
    right = ""

    for j in range(28): 
        left += key[leftSelection[j] - 1] 
        right += key[rightSelection[j] - 1]
    
    for i in range(16):
        left = shift(left,i + 1)
        right = shift(right, i + 1)
        key = left+right        
        for j in keySelection: 
            keys[i] += key[j - 1]
        
    for i in range(16):
        print(f"key {i + 1}  : {keys[i]}")


if __name__ == "__main__":
    key = " 00010011 00110100 01010111 01111001 10011011 10111100 11011111 11110001 "
    key = key.replace(" ", "")
    main(key)

