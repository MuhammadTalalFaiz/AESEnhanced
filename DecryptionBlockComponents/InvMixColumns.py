def inverse_mix_columns(state):
    
    transformation_matrix = [
        [0x0e, 0x0b, 0x0d, 0x09],
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]
    ]
    
    # Apply inverse mix columns transformation
    new_state = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_state[i][j] = (
                multiply(transformation_matrix[i][0], state[0][j]) ^
                multiply(transformation_matrix[i][1], state[1][j]) ^
                multiply(transformation_matrix[i][2], state[2][j]) ^
                multiply(transformation_matrix[i][3], state[3][j])
            )
    return new_state
