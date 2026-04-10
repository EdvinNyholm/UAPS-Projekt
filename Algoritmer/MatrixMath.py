def MatrixMath(A, B):
    # A: n x m, B: m x p => Resultat: n x p
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):          # Gå igenom rader i A
        for j in range(cols_B):      # Gå igenom kolumner i B
            for k in range(cols_A):  # Matcha element (rad i A mot kolumn i B)
                result[i][j] += A[i][k] * B[k][j]
                
    return result