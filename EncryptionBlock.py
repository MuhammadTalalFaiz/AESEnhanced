def aes_encrypt(plaintext, key):
    
    padding_length = 16 - len(plaintext) % 16
    plaintext += bytes([padding_length]) * padding_length
    state = [[plaintext[i + 4 * j] for i in range(4)] for j in range(4)]
    
    
    round_keys = key
    
    
    state = add_round_key(state, round_keys[:4])
    
    
    for i in range(1, 10):
        state = substitute_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)  
        state = add_round_key(state, round_keys[4*i:4*(i+1)])
    
    
    state = substitute_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[40:])
    
    return state
