import uvicorn
import shutil
import json
import os

from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware

from scripts import csv_to_xes, xes_dfg

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
    filename, _ = os.path.splitext(file)

    upload_path = f"../data/uploads/{filename}.csv"
    xes_path = f"../data/xes/{filename}.xes"
    dfg_path = f"../data/dfg_json/{filename}.json"

    csv_to_xes(upload_path, xes_path)
    dfg = xes_dfg(xes_path)

    with open(dfg_path,"w") as f:
        json.dump(dfg,f)

    return {"message": "File processed successfully."}

@app.get("/getDFG/")
async def getDFG(file: str):
    dfg_path = f"../data/dfg_json/{file}"

    with open(dfg_path, "r") as f:
        dfg_data = json.load(f)

    return {"dfg": dfg_data}

@app.get("/getDFGFiles")
async def get_files():
    dfg_dir = "../data/dfg_json/"
    try:
        files = [f for f in os.listdir(dfg_dir) if f.endswith('.json')]
        return files
    except Exception as e:
        return {"error": str(e)}
        # Returning an error mes


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0",port=8000)

