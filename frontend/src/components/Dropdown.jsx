import { useEffect, useState } from 'react';
import api from '../api'
import Graph from './Graph'


function Dropdown({filesList}){
  
  return (
  <div>
    <label htmlFor="dropdown">Select a File:</label>
    <select id="dropdown" name="dropdown">
      
      {filesList.map((file,index)=>
        <option key={index}>{file}</option>
      )}
    </select>
    
  </div>

  )
  
};

export default Dropdown;
