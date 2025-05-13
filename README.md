# 🎼 DNA ↔ MIDI Conversion Engine

This FastAPI-based app allows users to explore the complex musical structures hidden in DNA using concepts from genetic computation and musical theory.

## Features

- 🔄 Convert binary data → DNA
- 🎵 Sonify DNA using:
  - **Regulatory regions** (tempo & instrument control)
  - **Repetitive sequences** (loops, canons)
  - **Mutations/SNPs** (dissonance, modulations)
  - **Introns** (rests, ambient textures)
- ⏎ Convert MIDI back into DNA
- 💻 Simple web interface

## Usage

```bash
pip install fastapi uvicorn mido python-multipart jinja2
uvicorn main:app --reload
Then open your browser at: http://127.0.0.1:8000