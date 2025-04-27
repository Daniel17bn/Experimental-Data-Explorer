import uvicorn
import shutil

from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware

from scripts import csv_to_xes, xes_dfg

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"../data/uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"file '{file.filename}' saved"}


@app.post("/processfile/")
async def process_file(file:str):
    upload_path = f"../data/uploads/{file}"
    xes_path = f"../data/xes/{file.split(".")[0]}.xes"

    csv_to_xes(upload_path, xes_path)
    dfg = xes_dfg(xes_path)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0",port=8000)

