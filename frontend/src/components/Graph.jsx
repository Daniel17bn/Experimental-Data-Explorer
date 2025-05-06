import React, { useEffect } from 'react';
import cytoscape from 'cytoscape';
import api from '../api'; // Axios instance for API calls

const Graph = () => {
  useEffect(() => {
    // Fetch the example.json file from the backend
    api.get('/getDFG?file=test.json')
      .then((response) => {
        const data = response.data.dfg; // Extract the DFG data
        if (!data || !data.nodes || !data.edges) {
          throw new Error('Invalid data format');
        }

        // Initialize Cytoscape with the fetched data
        cytoscape({
          container: document.getElementById('cy'), // Container to render the graph
          elements: [
            ...data.nodes.map((node) => ({ data: { id: node.id, label: node.label } })),
            ...data.edges.map((edge) => ({
              data: {
                source: edge.source,
                target: edge.target,
                label: edge.label || '',
              },
            })),
          ],
          style: [
            {
              selector: 'node',
              style: {
                label: 'data(label)',
                'background-color': '#0074D9',
                color: '#fff',
                'text-valign': 'center',
                'text-halign': 'center',
              },
            },
            {
              selector: 'edge',
              style: {
                'line-color': '#FF4136',
                'target-arrow-color': '#FF4136',
                'target-arrow-shape': 'triangle',
                'curve-style': 'bezier',
                label: 'data(label)',
              },
            },
          ],
          layout: {
            name: 'grid', // Simple grid layout
          },
        });
      })
      .catch((error) => {
        console.error('Error fetching graph data:', error);
      });
  }, []);

  return <div id="cy" style={{ width: '100%', height: '600px' }} />;
};

export default Graph;
