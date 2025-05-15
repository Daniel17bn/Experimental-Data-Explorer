import {useState} from 'react';
import api from '../api';


function FileUploader({setFilesList}){

    const [file, setFile] = useState(null);

    function handleFileChange(event) {
        try{
            if (event.target.files){
                const currentFile = event.target.files[0]
                const fileName = currentFile.name.toLowerCase();
                if(fileName.endsWith('.csv')){
                    setFile(currentFile);
                }else{
                    alert('Please upload a valid CSV file.')
                }
                
            }
        } catch (error){
            console.log("Error:",error)

        }
    }

    
    async function handleUpload(event){
        const formData = new FormData();
        formData.append("file", file);

        try {
            
            await api.post('/uploadfile/',formData,{
                headers: {
                    'Content-Type': 'multipart/form-data', // Set the content type for file uploads
                }
            });
            console.log("Success uploading the file!");
            await api.post('/processfile/', {
                file_name: file.name,
            });
            await getFilesList();
        
        } catch (error){
            console.log("Error:",error);
        }
       
        setFile(null);

    }

    async function getFilesList(){
        try{
            const response = await api.get('/getFilesList/');
            const fileList = response.data.files
            setFilesList(fileList);
            console.log(fileList);

        } catch (error){
            console.log("Error:",error)
        }
    }

    return (
        <div>
            <input type="file" onChange={handleFileChange}></input>
            {file && <button onClick={handleUpload}>Upload File</button>}
            
        </div>
    );
};

export default FileUploader;