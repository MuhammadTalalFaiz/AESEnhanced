def aes_decrypt(ciphertext, round_key):
    
    state = [[ciphertext[i + 4 * j] for i in range(4)] for j in range(4)]
    
   
    round_keys = round_key
    
    
    state = add_round_key(state, round_keys[40:])
    
    
    for i in range(9, 0, -1):
        state = inverse_shift_rows(state)
        state = inverse_substitute_bytes(state)
        state = add_round_key(state, round_keys[4*i:4*(i+1)])
        state = inverse_mix_columns(state)  
    
    
    state = inverse_shift_rows(state)
    state = inverse_substitute_bytes(state)
    state = add_round_key(state, round_keys[:4])
    
    return state
