from fastapi import FastAPI, Request, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import shutil
from pathlib import Path

from dna_engine import encode_dna, dna_to_midi, midi_to_dna

app = FastAPI()

# Configurazione per servire file statici (come favicon)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_files(
    request: Request,
    binary_file: UploadFile = None,
    dna_file: UploadFile = None,
    midi_file: UploadFile = None
):
    output_path = Path("output")
    output_path.mkdir(exist_ok=True)

    result_message = ""

    if binary_file:
        contents = await binary_file.read()
        dna_result = encode_dna(contents)
        dna_path = output_path / "encoded_dna.txt"
        with open(dna_path, "w") as f:
            f.write(dna_result)
        result_message += f"✅ File binario convertito in DNA: <a href='/download/{dna_path.name}'>Scarica</a><br>"

    if dna_file:
        contents = await dna_file.read()
        dna_str = contents.decode("utf-8")
        midi_path = output_path / "output.mid"
        dna_to_midi(dna_str, str(midi_path))
        result_message += f"✅ DNA convertito in MIDI: <a href='/download/{midi_path.name}'>Scarica</a><br>"

    if midi_file:
        with open("temp.mid", "wb") as f:
            f.write(await midi_file.read())
        dna_result = midi_to_dna("temp.mid")
        dna_path = output_path / "midi_to_dna.txt"
        with open(dna_path, "w") as f:
            f.write(dna_result)
        result_message += f"✅ MIDI convertito in DNA: <a href='/download/{dna_path.name}'>Scarica</a><br>"

    return HTMLResponse(f"<html><body>{result_message}<br><a href='/'>🔙 Torna indietro</a></body></html>")

@app.get("/download/{filename}")
def download(filename: str):
    return FileResponse(path=f"output/{filename}", filename=filename)
