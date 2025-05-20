
function QstDropdown({qstList,setSelectedQst}){

    function handleClick(event){
        setSelectedQst(event.target.value);
    }

    return (
  
    <div className="dropdown"> {qstList.length > 0 && (
        <div>
        <label htmlFor="dropdown">Select a Questionnaire:</label>
        <select id="dropdown" name="dropdown">
            
            {qstList.map((file,index)=>
            <option key={index} onClick={handleClick}>{file}</option>
            )}
        </select>
        
        </div>
        )}
    </div>
    )
}

export default QstDropdown;