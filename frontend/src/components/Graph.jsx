import { useState, useEffect } from 'react';
import api from '../api';
import CytoscapeComponent from 'react-cytoscapejs';
import dagre from 'cytoscape-dagre';
import cytoscape from 'cytoscape';


cytoscape.use(dagre)

function Graph({selectedFile}) {
  const [data,setData] = useState(null);
  const [error,setError] = useState(null);

  useEffect(() => {
    setData(null)
    setError(null)
    api
      .get('/getDFG/', {
        params: {
          file: selectedFile + '.json'
        }
      })
      .then((response) => {
        setData(response.data);
      })
      .catch((err) => {
        console.error('Error fetching DFG:', err);
        setError('Failed to fetch DFG data.');
      });
  },[selectedFile])

  if (error) {
    return <div>{error}</div>
  }

  if (!data){
    return <div>Loading...</div>
  }

  const elements = [
    ...data.nodes.map((node) => ({data: node.data})),
    ...data.edges.map((edge) => ({data: edge.data}))
  ]
  

  return (
    <div className='graph'>
    <CytoscapeComponent
      elements={elements}
      style={{ width: '1300px', height: '500px' }}
      stylesheet={[
        {
          selector: 'node',
          style: {
            
            'background-color' : '#1a237e',
            'label' : 'data(label)',
            'color': 'black',
            'text-valign': 'top',
            'text-halign': 'center',
            'font-size': 12

          }
        },
        {
          selector: 'edge',
          style: {
            'width': 3,
            'line-color': '#ccc',
            'target-arrow-color': '#ccc',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'font-size': 10
          }
        }
      ]}
      layout={
        {
          name: 'dagre',
          rankDir: 'LR', 
          nodeSep: 50,   
          edgeSep: 10,  
          rankSep: 100,  
          animate: true
        }
      }
    />
    </div>
  );
}

export default Graph;