# 3DEN LAB - Documentazione

Benvenuto in **3DEN LAB**, un laboratorio virtuale per la codifica e la decodifica di sequenze genetiche, l'analisi tramite DNA Computing e la generazione di musica elettronica da sequenze DNA.

## Come interagire con il server

Il server fornisce vari endpoint che puoi utilizzare per eseguire operazioni legate al DNA Computing. Ecco alcune delle opzioni principali:

### 1. `/encode_dna`
- **Descrizione**: Codifica una sequenza DNA in un formato binario.
- **Metodo**: `GET`
- **Esempio di richiesta**: `GET /encode_dna?sequence=ATGC`

### 2. `/decode_dna`
- **Descrizione**: Decodifica una sequenza binaria in DNA.
- **Metodo**: `GET`
- **Esempio di richiesta**: `GET /decode_dna?binary=101110`

### 3. `/music_from_dna`
- **Descrizione**: Trasforma una sequenza DNA in un file musicale MIDI.
- **Metodo**: `GET`
- **Esempio di richiesta**: `GET /music_from_dna?sequence=ATGC`

### 4. `/help`
- **Descrizione**: Mostra tutte le opzioni disponibili e i comandi.
- **Metodo**: `GET`
