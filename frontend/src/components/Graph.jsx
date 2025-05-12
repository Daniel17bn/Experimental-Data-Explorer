import { useState, useEffect } from 'react';
import api from '../api';
import CytoscapeComponent from 'react-cytoscapejs';
import dagre from 'cytoscape-dagre';
import cytoscape from 'cytoscape';
import '../App.css';

cytoscape.use(dagre)

function Graph() {
  const [data,setData] = useState(null);
  const [error,setError] = useState(null);

  useEffect(() => {
    api
      .get('/getDFG/', {
        params: {
          file: 'experiment_log.json'
        }
      })
      .then((response) => {
        setData(response.data);
      })
      .catch((err) => {
        console.error('Error fetching DFG:', err);
        setError('Failed to fetch DFG data.');
      });
  },[])

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
    <CytoscapeComponent
      elements={elements}
      style={{ width: '1300px', height: '500px' }}
      stylesheet={[
        {
          selector: 'node',
          style: {
            
            'background-color' : 'rgba(23, 49, 86, 0.7)',
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
          rankDir: 'LR', // LR = Left to Right (or use 'TB' for Top to Bottom)
          nodeSep: 50,   // spacing between nodes
          edgeSep: 10,   // spacing between edges
          rankSep: 100,  // spacing between layers
          animate: true
        }
      }
    />
  );
}

export default Graph;