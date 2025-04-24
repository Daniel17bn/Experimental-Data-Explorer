import React from 'react';
import CytoscapeComponent from 'react-cytoscapejs';

const Graph = () => {
  const elements = [
    { data: { id: 'A', label: 'Node A' } },
    { data: { id: 'B', label: 'Node B' } },
    { data: { source: 'A', target: 'B', label: 'Edge A-B' } }
  ];

  return (
    <CytoscapeComponent
      elements={elements}
      style={{ width: '100%', height: '500px' }}
      layout={{ name: 'breadthfirst' }}
      stylesheet={[
        {
          selector: 'node',
          style: {
            label: 'data(label)',
            'background-color': '#0074D9',
            'text-valign': 'center',
            color: '#fff',
            'text-outline-color': '#0074D9',
            'text-outline-width': 2,
          }
        },
        {
          selector: 'edge',
          style: {
            label: 'data(label)',
            'target-arrow-shape': 'triangle',
            'line-color': '#ccc',
            'target-arrow-color': '#ccc',
            'curve-style': 'bezier',
            width: 2,
          }
        }
      ]}
    />
  );
};

export default Graph;
