def deduce_key(round_keys):
    original_master_key = round_keys[:4]
    W6 = round_keys[5]
    W7 = round_keys[6]
    Possibilities = 2**64
    Counter = 0
    
    for w1 in range(2**32):  
        w1_bytes = [(w1 >> (8 * (3 - i)) & 0xFF) for i in range(4)]  
        
        for w4 in range(2**32):  
            w4_bytes = [(w4 >> (8 * (3 - i)) & 0xFF) for i in range(4)] 
            
            W5 = [w1_byte ^ w4_byte for w1_byte, w4_byte in zip(w1_bytes, g(w4_bytes,1))] 
            

            
            W6_padded = W6 + [0] * (4 - len(W6))  
            W2 = [W6_byte ^ W5_byte for W6_byte, W5_byte in zip(W6_padded, W5)]

            
            W7_padded = W7 + [0] * (4 - len(W7)) 
            W3 = [W7_byte ^ W5_byte for W7_byte, W5_byte in zip(W7_padded, W5)]

            Counter += 1
            deduced_key = [w1_bytes] + [W2] + [W3]+ [w4_bytes]
            print("Progress: ", Counter, "/", Possibilities)
            
            
            if deduced_key == original_master_key:
                return deduced_key

    return None
