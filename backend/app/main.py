import uvicorn
import os
import shutil

from fastapi import FastAPI,File,UploadFile,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from scripts.csv_to_xes import csv_to_xes
from scripts.xes_dfg import xes_dfg


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

IMPORT_FOLDER = "backend/data/raw"
PROCESSED_FOLDER = "backend/data/xes"
DFG_FOLDER = "backend/data/dfg_json"

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(IMPORT_FOLDER, file.filename)
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename:": file.filename, "file_location": file_location} 


@app.post("/process/")
async def process_file(background_tasks: BackgroundTasks, filename: str):
    input_path = os.path.join(IMPORT_FOLDER, filename)
    output_path = os.path.join(PROCESSED_FOLDER, filename.replace(".csv", ".xes"))

    if not os.path.exists(input_path):
        return {"error": "File not found"}

    background_tasks.add_task(csv_to_xes, input_path, output_path)

    return {"message": f"Processing started for {filename}"}

#Not completed yet
@app.get("/getDFG")
async def get_dfg(filename: str):

    input_path = os.path.join(DFG_FOLDER, filename)

    if not os.path.exists(input_path):
        return {"error": "File not found"}

    try:
        dfg = xes_dfg(input_path)
        
        return {
            "filename": filename,
            "dfg": dfg,
            "status": "success"
        }
    except Exception as e:
        return {
            "error": f"Failed to process XES file: {str(e)}",
            "status": "error"
        }





if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0",port=8000)

