import uvicorn
import shutil
import json
import os
import logging

from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from pydantic import BaseModel
from scripts import csv_to_xes, xes_dfg,process_qst


BASE_PATH = Path(__file__).resolve().parent
DATA_PATH = BASE_PATH.parent / "data"
UPLOADS_PATH = DATA_PATH / "uploads"
XES_PATH = DATA_PATH / "xes"
DFG_PATH = DATA_PATH / "dfg_json"
QST_PATH = DATA_PATH / "qst_json"


UPLOADS_PATH.mkdir(parents=True, exist_ok=True)
XES_PATH.mkdir(parents=True, exist_ok=True)
DFG_PATH.mkdir(parents=True, exist_ok=True)
QST_PATH.mkdir(parents=True, exist_ok=True)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(UPLOADS_PATH / file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"file '{file.filename}' saved"}


class FileNameRequest(BaseModel):
    file_name: str

@app.post("/processfile/")
async def process_file(request: FileNameRequest):

    logger.info(f"/processfile/: Received the request: {request}")
    file_name = request.file_name
    filename, _ = os.path.splitext(file_name)



    upload_path = UPLOADS_PATH / file_name
    xes_path = XES_PATH / f'{filename}.xes'
    dfg_path = DFG_PATH
    dfg_name = f'{filename}.json'
    qst_path = QST_PATH / f'{filename}.json'


    if not os.path.exists(upload_path):
        return {"error": f"File '{upload_path}' does not exist. Please upload it first."}


    try:
        logger.info(f"/processfile/: Processing the CSV to XES ({upload_path} -> {xes_path})")
        csv_to_xes(upload_path, xes_path)

        logger.info(f"/processfile/: Generating the DFG from the XES")


        dfg = xes_dfg(str(xes_path),str(dfg_path),str(dfg_name))

    except Exception as e:
        if str(e) == "the dataframe should (at least) contain a column for the case identifier, a column for the activity and a column for the timestamp.":
            process_qst(upload_path,qst_path)
        else:
            return {"error": f"An error occurred during processing: {str(e)}"}


    return {"message": "File processed successfully."}

@app.get("/getDFG/")
async def getDFG(file: str):
    dfg_path = DFG_PATH / f'{file}'


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

@app.get("/getQst/")
async def get_Qst(file:str):
    csv_path = UPLOADS_PATH / f"{file}"
    qst_path = QST_PATH / f"{file.split('.')[0]}.json"

    try:
        if not os.path.exists(qst_path):
            if not os.path.exists(csv_path):
                return {"error": f"File '{file}' does not exist in the uploads directory."}
            process_qst(csv_path,qst_path)

        with open(qst_path,"r") as f:
            qst_data = json.load(f)



    except Exception as e:
        return {"error": f"An error occurred while processing the file: {str(e)}"}

    return qst_data

@app.get("/getQstList/")
async def get_qstFiles():
    qst_dir = QST_PATH
    try:
        files = [f for f in os.listdir(qst_dir) if os.path.isfile(os.path.join(qst_dir, f))]
        for i in range(len(files)):
            files[i] = files[i].split(".")[0]
    except FileNotFoundError:
        return {"error": f"Directory '{qst_dir}' does not exist."}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
    return {'files': files}



if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0",port=8000)

