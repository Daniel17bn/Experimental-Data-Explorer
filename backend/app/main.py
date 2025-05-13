import uvicorn
import shutil
import json
import os
import logging

from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from pydantic import BaseModel
from scripts import csv_to_xes, xes_dfg

# Setup main paths
BASE_PATH = Path(__file__).resolve().parent
DATA_PATH = BASE_PATH.parent / "data"
UPLOADS_PATH = DATA_PATH / "uploads"
XES_PATH = DATA_PATH / "xes"
DFG_PATH = DATA_PATH / "dfg_json"

## Make sure that the folders also exist
UPLOADS_PATH.mkdir(parents=True, exist_ok=True)
XES_PATH.mkdir(parents=True, exist_ok=True)
DFG_PATH.mkdir(parents=True, exist_ok=True)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    with open(UPLOADS_PATH / file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"file '{file.filename}' saved"}

# Define the Pydantic model for the request body
class FileNameRequest(BaseModel):
    file_name: str

@app.post("/processfile/")
async def process_file(request: FileNameRequest):

    logger.info(f"/processfile/: Received the request: {request}")
    file_name = request.file_name  # Extract the file name from the request
    filename, _ = os.path.splitext(file_name)  # Extract the filename without extension

    # Define paths

    upload_path = UPLOADS_PATH / file_name # f"../data/uploads/{file_name}"
    xes_path = XES_PATH / f'{filename}.xes' # f"../data/xes/{filename}.xes"
    dfg_path = DFG_PATH                   # f"../data/dfg_json/{filename}.json"
    dfg_name = f'{filename}.json' # f"../data/dfg_json/{filename}.json"

    # Check if the uploaded file exists
    if not os.path.exists(upload_path):
        return {"error": f"File '{upload_path}' does not exist. Please upload it first."}

    # Process the file
    try:
        logger.info(f"/processfile/: Processing the CSV to XES ({upload_path} -> {xes_path})")
        csv_to_xes(upload_path, xes_path)  # Convert CSV to XES

        logger.info(f"/processfile/: Generating the DFG from the XES")

        # Have to convert from Path to string here since i think pm4py does not support it
        dfg = xes_dfg(str(xes_path),str(dfg_path),str(dfg_name))  # Generate the DFG

    except Exception as e:
        return {"error": f"An error occurred during processing: {str(e)}"}

  
    return {"message": "File processed successfully."}

@app.get("/getDFG/")
async def getDFG(file: str):
    dfg_path = DFG_PATH / f'{file}'

    # Check if the file exists
    if not os.path.exists(dfg_path):
        return {"error": f"File '{file}' does not exist in the directory."}

    try:
        with open(dfg_path, "r") as f:
            dfg_data = json.load(f)
    except json.JSONDecodeError:
        return {"error": f"File '{file}' is not a valid JSON file."}
    except Exception as e:
        return {"error": f"An error occurred while reading the file: {str(e)}"}

    return dfg_data

@app.get("/getFilesList")
async def get_files():
    dfg_dir = DFG_PATH
    try:
        files = [f for f in os.listdir(dfg_dir) if os.path.isfile(os.path.join(dfg_dir, f))]
        for i in range(len(files)):
            files[i] = files[i].split(".")[0]
    except FileNotFoundError:
        return {"error": f"Directory '{dfg_dir}' does not exist."}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    return {'files': files}



if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0",port=8000)

