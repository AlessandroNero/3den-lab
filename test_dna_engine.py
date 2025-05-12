from dna_engine import encode_to_dna

def test_encoding():
    result = encode_to_dna("A")
    print(f"DNA encoding of 'A': {result}")

if __name__ == "__main__":
    test_encoding()
