def int_to_binary(num, minlen=8):
    binary = []
    temp = bin(num)[1:]
    for c in temp:
        if c == '0':
            binary.append(0)
        elif c == '1':
            binary.append(1)
    ap = []
    if len(binary) < minlen:
        for i in range(minlen - len(binary)):
            ap.append(0)

    ap.extend(binary)
    return ap


def hex_to_binary(str):
    binary = []
    byte_array = bytes.fromhex(str)
    for x in byte_array:
        if x is not None:
            binary.extend(int_to_binary(x))
    return binary


def text_to_binary_(str):
    binary = []
    byte_array = bytearray(str, encoding='utf-8')
    for x in byte_array:
        binary.extend(int_to_binary(x))

    return binary


def pc1(binaryKey):
    if len(binaryKey) != 64:
        return None
    pc1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]
    newbinary = []
    for i in pc1:
        newbinary.append(binaryKey[i - 1])
    return newbinary


def pc2(binaryKey):
    if len(binaryKey) != 56:
        return None
    pc2 = [14, 17, 11, 24, 1, 5, 3,28,
           15, 6, 21, 10, 23, 19, 12, 4,
           26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40,
           51, 45, 33, 48, 44, 49, 39, 56,
           34, 53, 46, 42, 50, 36, 29, 32]
    newbinary = []
    for i in pc2:
        newbinary.append(binaryKey[i - 1])
    return newbinary


def ip(binary):
    if len(binary) != 64:
        return None
    ip = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    newbinary = []
    for i in ip:
        newbinary.append(binary[i - 1])
    return newbinary


def E(binary):
    if len(binary) != 32:
        return None
    E = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20,
         21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    newbinary = []
    for i in E:
        newbinary.append(binary[i - 1])
    return newbinary


def S(binary):
    if len(binary) != 48:
        return None
    afterSBinary = []
    s1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    s2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    S = s1, s2, s3, s4, s5, s6, s7, s8
    for i in range(8):
        start = i * 6
        end = start + 5
        row = binary_to_int([binary[start], binary[end]])
        col = binary_to_int(binary[start + 1:end])
        # print(binary[start + 1:end ])
        # print('i:{}'.format(i))
        # print('row:{}'.format(row))
        # print('col:{}'.format(col))
        afterSBinary.extend(int_to_binary(S[i][row][col],minlen=4))

    return afterSBinary


def P(binary):
    if len(binary) != 32:
        return None
    P = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]
    newbinary = []
    for i in P:
        newbinary.append(binary[i - 1])
    return newbinary


def xor(a,b):
    c=[]
    if len(a)!=len(b):
        return None
    for i in range(len(a)):
        if a[i]==b[i]:
            c.append(0)
        else:
            c.append(1)
    return c


def binary_to_int(binary):
    return int("".join(str(x) for x in binary), 2)


def shift_left(binary):
    if binary is None:
        return None
    if len(binary) <= 1:
        return binary
    binary2 = binary[1:]
    binary2.append(binary[0])
    return binary2

def round1(text , key):
    text = ip(hex_to_binary(text))
    print('Text in Binary After IP Table')

    print('Left')
    left = text[:32]
    display(left)

    right = text[32:]
    print('\nRight')
    display(right)
    left2 = right.copy()

    key=text_to_binary_(key)
    print('\nKey in Binary')
    display(key)

    if len(key)==64:

        key=pc1(key)
        print('\nKey After PC1')
        display(key,7)

        key=shift_left(key)
        print('\nKey After Left Shift')
        display(key,7)

    key=pc2(key)
    print('\nKey After PC2')
    display(key)

    right=E(right)
    print('\nRight After E Table')
    display(right)

    right=xor(right,key)
    print('\nRight After XOR With Key')
    display(right)

    right=S(right)
    print('\nRight After S Table')
    display(right)

    right=P(right)
    print('\nRight After P Table')
    display(right)

    right2=xor(right,left)
    print('\nRight After XOR with Left')
    display(right2)

    print('\nEnd Of Round')
    print("Left")
    display(left2)

    print("\nRight")
    display(right2)

    left2.extend(right2)
    return text


def display(key,endl=8):
    for i in range(len(key)):
        if i % endl == 0:
            print()
        print(key[i], end=' ')


text = 'F9B826521DEA7B4C'
key="IT16A037"
round1(text,key)

# text = 'F9B826521DEA7B4C'
# text=hex_to_binary(text)
# print(len(text))
# right=text[:48]
# print(len(right))
# display(right,endl=6)
# print('After S')
# display(S(right))
