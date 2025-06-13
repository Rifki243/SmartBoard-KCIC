from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
from model import load_model, predictface
import os

app = FastAPI()

# Load model saat server start
model = load_model()

# Mount folder front-end
app.mount("/static", StaticFiles(directory="../front-end"), name="static")

@app.post("/auto-detect/")
async def auto_detect(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    input_type = "auto"
    name, ticket, schedule, message, box, sisa_waktu = predictface(img, model, input_type)
    return {
        "name": name,
        "ticket": ticket,
        "schedule": schedule,
        "message": message,
        "box": box,
        "sisa_waktu": sisa_waktu
    }

@app.get("/")
async def read_root():
    file_path = os.path.join("..", "front-end", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)