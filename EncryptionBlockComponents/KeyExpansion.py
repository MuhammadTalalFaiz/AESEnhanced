import random 
def key_expansion(key, round_constants, Q):
    round_keys = [key[i:i+4] for i in range(0, len(key), 4)]
    
    for i in range(Q):
        for j in range(4):
            
            new_key = [round_keys[-4][k] ^ round_keys[-3][k] ^ round_keys[-2][k] for k in range(4)]
            new_key = complex_operation(new_key, round_constants[i])
            random_word = generate_random_word()
            new_key = [new_key[k] ^ random_word[k] for k in range(4)]
            round_keys.extend([new_key])
    
    return round_keys

def complex_operation(word, round_constant):
    
    word = word[1:] + [word[0]]
    word = [S_BOX[b] for b in word]
    word[0] ^= round_constant
    
    return word

def generate_random_word():
    
    return [random.randint(0, 255) for _ in range(4)]
