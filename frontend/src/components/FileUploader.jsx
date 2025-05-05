import React, {useState, ChangeEvent} from 'react';

const UploadStatus = {
    IDLE: "idle",
    UPLOADING: "uploading",
    SUCCESS: "success",
    ERROR: "error"
};

function FileUploader(){

    const [file, setFile] = useState(null);
    const [status,setStatus] = useState(UploadStatus.IDLE)

    function handleFileChange(event) {
        if (event.target.files){
            setFile(event.target.files[0]);
            setStatus(UploadStatus.UPLOADING);

        }
    }


    return (
        <div>
            <input type="file" onChange= {handleFileChange}/>
            {file && status !== UploadStatus.IDLE && <button>Upload File</button>}


        </div>
    );
};

export default FileUploader;