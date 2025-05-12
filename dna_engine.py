# dna_engine.py
from midiutil import MIDIFile

# Mappatura DNA↔bit
BIT_TO_DNA = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
}
DNA_TO_BIT = {v: k for k, v in BIT_TO_DNA.items()}

# Mappatura DNA↔MIDI note
DNA_TO_MIDI_NOTE = {
    'A': 60,  # Do
    'C': 62,  # Re
    'G': 64,  # Mi
    'T': 65   # Fa
}
MIDI_NOTE_TO_DNA = {v: k for k, v in DNA_TO_MIDI_NOTE.items()}


def encode_dna(file_bytes: bytes) -> str:
    binary = ''.join(f"{byte:08b}" for byte in file_bytes)
    dna = ''.join(BIT_TO_DNA[binary[i:i+2]] for i in range(0, len(binary), 2))
    return dna


def dna_to_midi(dna_sequence: str, output_path: str):
    midi = MIDIFile(1)
    midi.addTempo(0, 0, 120)
    time = 0
    for base in dna_sequence:
        note = DNA_TO_MIDI_NOTE.get(base)
        if note:
            midi.addNote(0, 0, note, time, 1, 100)
            time += 1
    with open(output_path, "wb") as output_file:
        midi.writeFile(output_file)


def midi_to_dna(midi_path: str) -> str:
    from mido import MidiFile
    mid = MidiFile(midi_path)
    dna_seq = ""
    for msg in mid:
        if msg.type == 'note_on' and msg.velocity > 0:
            dna_base = MIDI_NOTE_TO_DNA.get(msg.note)
            if dna_base:
                dna_seq += dna_base
    return dna_seq
