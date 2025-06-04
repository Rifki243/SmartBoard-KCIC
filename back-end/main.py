from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from model import load_model, predict_face
import os

app = FastAPI()
model = load_model()

# Menyajikan file statis dari direktori front-end
app.mount("/static", StaticFiles(directory="../front-end"), name="static")

@app.post("/upload-photo/")
async def upload_photo(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Menentukan jenis input
    input_type = "upload"
    name, ticket, schedule, message = predict_face(img, model, input_type)
    return {"name": name, "ticket": ticket, "schedule": schedule, "message": message}

@app.post("/capture-frame/")
async def capture_frame(file: UploadFile = File(...)):
    # Di sini kita akan menggunakan gambar dari video
    input_type = "capture"
    # Untuk saat ini, kita akan mengembalikan hasil dummy
    img = None  # Gambar dari kamera (di sini kita tidak memproses gambar nyata)
    name, ticket, schedule, message = predict_face(img, model, input_type)
    return {"name": name, "ticket": ticket, "schedule": schedule, "message": message}

@app.get("/")
async def read_root():
    file_path = os.path.join("..", "front-end", "index.html")
    return HTMLResponse(content=open(file_path).read())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
