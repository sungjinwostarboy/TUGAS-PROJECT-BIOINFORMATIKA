def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    m, n = len(seq1), len(seq2)
    score = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        score[i][0] = i * gap
    for j in range(n+1):
        score[0][j] = j * gap

    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = score[i-1][j-1] + (match if seq1[i-1]==seq2[j-1] else mismatch)
            delete = score[i-1][j] + gap
            insert = score[i][j-1] + gap
            score[i][j] = max(diag, delete, insert)
    
    return score, score[m][n]

def smith_waterman(seq1, seq2, match=3, mismatch=-3, gap=-2):
    m, n = len(seq1), len(seq2)
    score = [[0]*(n+1) for _ in range(m+1)]
    max_score = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            diag = score[i-1][j-1] + (match if seq1[i-1]==seq2[j-1] else mismatch)
            delete = score[i-1][j] + gap
            insert = score[i][j-1] + gap
            score[i][j] = max(0, diag, delete, insert)
            max_score = max(max_score, score[i][j])
    
    return score, max_score
