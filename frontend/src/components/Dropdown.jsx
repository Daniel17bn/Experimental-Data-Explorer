import { useEffect, useState } from 'react';
import api from '../api'
import Graph from './Graph'


function Dropdown({filesList,setSelectedFile}){

  function handleClick(event){
    setSelectedFile(event.target.value);
  }
  
  return (
  
   <div className="dropdown"> {filesList.length > 0 && (
    <div>
    <label htmlFor="dropdown">Select a File:</label>
      <select id="dropdown" name="dropdown">
        
        {filesList.map((file,index)=>
          <option key={index} onClick={handleClick}>{file}</option>
        )}
      </select>
    
    </div>
      )}
   </div>
    
  
  )
  
};

export default Dropdown;
