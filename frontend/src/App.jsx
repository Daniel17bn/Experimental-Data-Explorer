import React, {useState} from 'react';
import FileUploader from './components/FileUploader';
import Graph from './components/Graph';
import DropDown from './components/DropDown';
import './App.css';

function App() {

    const [filesList,setFilesList] = useState([]);
    const [selectedFile,setSelectedFile] = useState(null)

    return (
        <>
            <h1>BSP Project</h1>
            <div>
                <FileUploader setFilesList={setFilesList}/>
                <DropDown filesList={filesList} setSelectedFile={setSelectedFile}/>
            </div>
            <div style={{ marginTop: '2rem' }}>
                <h2>Directly Follows Graph</h2>
                {selectedFile != null && <Graph selectedFile={selectedFile}></Graph>}
                
            </div>
        </>
    );
}

export default App;
