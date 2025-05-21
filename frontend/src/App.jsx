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
    const [showDropdowns, setShowDropdowns] = useState(false);


    return (
        <>
          <h1>Experimental Data Explorer</h1>
          <FileUploader
            setFilesList={setFilesList}
            setQstList={setQstList}
            onUploadSuccess={() => setShowDropdowns(true)}
          />
          {showDropdowns && (
            <div className="dropdown-row">
              <DropDown filesList={filesList} setSelectedFile={setSelectedFile}/>
              <QstDropdown qstList={qstList} setSelectedQst={setSelectedQst}/>
            </div>
          )}
          <div style={{ marginTop: '2rem' }}>
            {selectedFile != null && <Graph selectedFile={selectedFile}></Graph>}
          </div>
          <div>
            {selectedQst != null && <Questionnaire selectedQst={selectedQst}/>}
          </div>
        </>
    );
}

export default App;
