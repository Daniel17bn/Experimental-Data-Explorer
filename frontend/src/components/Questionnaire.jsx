import {useEffect,useState} from 'react';
import api from '../api';

function Questionnaire(){

    const [data,setData] = useState(null);
    const [selectedFile,setSelectedFile] = useState('vr-questionnaire');
    const[selectedQuestionnaire,setSelectedQuestionnaire]=useState(null);
    const[selectedCondition,setSelectedCondition]=useState(null);

    useEffect( () => {
        
        api.get('/getQst/', {
        params: {
          file: selectedFile + '.json'
        }
      })
      .then((response) => {
        setData(response.data);
      })
      .catch((err) => {
        console.error('Error fetching Qst. :', err);
        setError('Failed to fetch Qst. data.');
      });
  },[selectedFile])

    if (!data) return(<div>Loading...</div>);

    return (
        <div className="questionnaire"> 
            <h1>Questionnaire</h1>
            {Object.entries(data).map(([questionnaire,conditions])=>(
                <div key={questionnaire}>
                    <h2 onClick={()=>setSelectedQuestionnaire(selectedQuestionnaire === questionnaire ? null : questionnaire)}
                        style={{cursor:'pointer',color: selectedQuestionnaire===questionnaire ? 'blue':'black'}}>
                        {questionnaire}
                    </h2>
                    {selectedQuestionnaire === questionnaire && 
                        Object.entries(conditions).map(([condition,questions])=>(
                        <div key={condition} >
                            <h3 onClick={()=>setSelectedCondition(selectedCondition === condition ? null : condition)}
                                style={{cursor:'pointer',color: selectedCondition===condition ? 'blue':'black'}}>
                                {condition}
                            </h3>
                            <ul>
                                {selectedCondition===condition && 
                                    questions.map((q)=>(
                                    <li key={q["Question Number"]}>
                                        <strong>Q{q["Question Number"]} :</strong> {q.Question}
                                        <br/>
                                        <strong>Answer:</strong>{q.Answer}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>
            ))}
        </div>
    )
}


export default Questionnaire;