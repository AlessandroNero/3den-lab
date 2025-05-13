from mido import MidiFile

# Reverse mapping of rhythm to codon
rhythm_codon_map = {
    (480, 240, 240): 'ATG',
    (120, 120, 480): 'TAA',
    (360, 120, 120): 'TGA',
    (240, 240, 240): 'TAG',
}

def map_midi_to_dna(midi_file_path):
    """
    Converts a MIDI file back into a DNA sequence.
    """
    mid = MidiFile(midi_file_path)
    dna_sequence = ''
    
    for track in mid.tracks:
        durations = []
        for msg in track:
            if msg.type == 'note_off':
                durations.append(msg.time)
                if len(durations) == 3:
                    rhythm_tuple = tuple(durations)
                    codon = rhythm_codon_map.get(rhythm_tuple, 'NNN')
                    dna_sequence += codon
                    durations = []
    
    return dna_sequence
