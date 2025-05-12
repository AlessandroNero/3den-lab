# dna_engine.py

def encode_to_dna(data: str) -> str:
    binary = ''.join(format(ord(char), '08b') for char in data)
    return binary_to_dna(binary)

def binary_to_dna(binary: str) -> str:
    dna = ""
    for i in range(0, len(binary), 2):
        pair = binary[i:i+2]
        if pair == "00":
            dna += "A"
        elif pair == "01":
            dna += "C"
        elif pair == "10":
            dna += "G"
        elif pair == "11":
            dna += "T"
    return dna
