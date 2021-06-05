def decrypt(c):
    if c == "AUG": return "Methionine"
    elif c == "UUU" or c == "UUC": return "Phenylalanine"
    elif c == "UUA" or c == "UUG": return "Leucine"
    elif c == "UCU" or c == "UCC" or c == "UCA" or c == "UCG": return "Serine"
    elif c == "UAU" or c == "UAC": return "Tyrosine"
    elif c == "UGU" or c == "UGC": return "Cysteine"
    elif c == "UGG": return "Tryptophan"
    else: return "STOP"

def proteins(strand):
    result = []
    for i in range(0, len(strand), 3):
        protein = decrypt(strand[i:i + 3])
        if protein == "STOP": break
        result.append(protein)
    return result
