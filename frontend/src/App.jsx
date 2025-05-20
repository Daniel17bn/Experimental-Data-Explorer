import {useState} from 'react';
import FileUploader from './components/FileUploader';
import Graph from './components/Graph';
import DropDown from './components/Dropdown';
import Questionnaire from './components/Questionnaire';
import QstDropdown from './components/QstDropdown'
import './App.css';

function App() {

    const [filesList,setFilesList] = useState([]);
    const [selectedFile,setSelectedFile] = useState(null);
    const [qstList,setQstList] = useState([]);
    const [selectedQst,setSelectedQst] = useState(null);


    return (
        <>
            <h1>BSP Project</h1>
            <div>
                <FileUploader setFilesList={setFilesList} setQstList={setQstList}/>
                <DropDown filesList={filesList} setSelectedFile={setSelectedFile}/>
                <QstDropdown qstList={qstList} setSelectedQst={setSelectedQst}/>
            </div>
            <div style={{ marginTop: '2rem' }}>
                <h2>Directly Follows Graph</h2>
                {selectedFile != null && <Graph selectedFile={selectedFile}></Graph>}
                
            </div>
            <div>
                {selectedQst != null && <Questionnaire selectedQst={selectedQst}/>}
            </div>
            
        </>
    );
}

export default App;
