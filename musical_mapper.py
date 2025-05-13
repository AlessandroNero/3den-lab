from mido import Message, MidiFile, MidiTrack, MetaMessage

def dna_to_complex_midi(dna: str, output_file: str):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    base_map = {'A': 60, 'T': 62, 'C': 64, 'G': 67}

    # Regulatory logic
    regulatory_regions = ['TATA', 'CAAT']
    repetitive_motifs = ['ATAT', 'CAGCAG']
    intron_markers = ['GT', 'AG']
    mutation_interval = 111
    mutation_shift = 5
    velocity = 64

    # Codon rhythm mapping
    codon_rhythm_map = {
        'ATG': [480, 240, 240],
        'TAA': [120, 120, 480],
        'TGA': [360, 120, 120],
        'TAG': [240, 240, 240],
    }

    # Gene pitch mapping (could be randomized per session or assigned dynamically)
    gene_pitch_map = {
        'gene1': [60, 62, 64, 65, 67],
        'gene2': [67, 65, 64, 62, 60],
        'unknown': [72, 71, 69, 67, 65],
    }

    tempo_base = 500000
    enhancer_toggle = 0
    note_duration = 240
    current_gene = 'unknown'

    # Detect tempo controllers
    for i in range(len(dna)):
        if dna[i:i+4] in regulatory_regions:
            tempo = tempo_base - (i % 4) * 50000
            track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
            enhancer_toggle = (enhancer_toggle + 1) % 127
            track.append(Message('program_change', program=enhancer_toggle, time=0))

    # Main loop
    i = 0
    while i < len(dna):
        codon = dna[i:i+3]
        if len(codon) < 3 or any(base not in base_map for base in codon):
            i += 1
            continue

        # Handle gene start / stop codons as gene identifiers
        if codon == 'ATG':
            current_gene = 'gene1'
        elif codon in ['TAA', 'TAG', 'TGA']:
            current_gene = 'gene2'

        rhythm = codon_rhythm_map.get(codon, [note_duration] * 3)
        pitches = gene_pitch_map.get(current_gene, gene_pitch_map['unknown'])

        # Apply repetitive motifs as layered repetitions
        for motif in repetitive_motifs:
            if dna[i:i+len(motif)] == motif:
                for _ in range(3):
                    for base in motif:
                        if base in base_map:
                            track.append(Message('note_on', note=base_map[base], velocity=velocity, time=0))
                            track.append(Message('note_off', note=base_map[base], velocity=velocity, time=note_duration))
                i += len(motif)
                break
        else:
            # Mutation injection
            if i % mutation_interval == 0:
                pitch_shift = mutation_shift
                track.append(MetaMessage('marker', text='mutation', time=0))
            else:
                pitch_shift = 0

            # Rhythm and pitch from codon
            for j in range(3):
                base = codon[j]
                pitch = base_map[base] + pitch_shift
                pitch += j  # For more variation
                pitch_set = pitches[j % len(pitches)]

                # Intron = ambient/rest
                if dna[i+j:i+j+2] in intron_markers:
                    track.append(Message('note_on', note=40, velocity=20, time=0))
                    track.append(Message('note_off', note=40, velocity=20, time=rhythm[j]))
                else:
                    track.append(Message('note_on', note=pitch_set, velocity=velocity, time=0))
                    track.append(Message('note_off', note=pitch_set, velocity=velocity, time=rhythm[j]))
            i += 3
