from Bio import SeqIO

def parse_dna(file_path):
    """
    Parses a DNA sequence file in FASTA or GenBank format.
    Returns a dictionary with sequence and features.
    """
    if file_path.endswith('.gb') or file_path.endswith('.gbk'):
        record = SeqIO.read(file_path, "genbank")
    else:
        record = SeqIO.read(file_path, "fasta")

    sequence = str(record.seq)
    features = []

    if hasattr(record, 'features'):
        for feature in record.features:
            features.append({
                'type': feature.type,
                'location': feature.location,
                'qualifiers': feature.qualifiers
            })

    return {
        'sequence': sequence,
        'features': features
    }
