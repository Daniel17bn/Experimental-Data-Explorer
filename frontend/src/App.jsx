import React, {useState} from 'react';
import FileUploader from './components/FileUploader';
import Graph from './components/Graph';
import DropDown from './components/DropDown';
import './App.css';

function App() {

    const [filesList,setFilesList] = useState([]);
    

    return (
        <>
            <h1>BSP Project</h1>
            <div>
                <FileUploader setFilesList={setFilesList}/>
                <DropDown filesList={filesList}/>
            </div>
            <div style={{ marginTop: '2rem' }}>
                <h2>Graph Visualization</h2>
                <div className='graph'>
                    <Graph/>
                </div>
                
            </div>
        </>
    );
}

export default App;
