def mix_columns(state):
    for i in range(4):
        s0 = state[0][i]
        s1 = state[1][i]
        s2 = state[2][i]
        s3 = state[3][i]
        
        state[0][i] = multiply(s0, 2) ^ multiply(s1, 3) ^ s2 ^ s3
        state[1][i] = s0 ^ multiply(s1, 2) ^ multiply(s2, 3) ^ s3
        state[2][i] = s0 ^ s1 ^ multiply(s2, 2) ^ multiply(s3, 3)
        state[3][i] = multiply(s0, 3) ^ s1 ^ s2 ^ multiply(s3, 2)
    return state

def multiply(a, b):
    
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B  
        b >>= 1
    return result
