import React, { useEffect } from 'react';
import cytoscape from 'cytoscape';
import dagre from 'cytoscape-dagre'; // Import dagre layout
import api from '../api'; // Import the Axios instance

cytoscape.use(dagre); // Register dagre layout

const Graph = () => {
  useEffect(() => {
    const fileName = 'example.json';

    // Use the Axios instance to fetch the graph data
    api.get(`/getDFG?file=${fileName}`)
      .then((response) => {
        const data = response.data; // Axios automatically parses JSON
        console.log('Parsed data:', data); // Log the parsed data
        console.log('Nodes data:', data.dfg.nodes); // Log nodes for debugging
        console.log('Edges data:', data.dfg.edges); // Log edges for debugging

        // Ensure the data structure matches the expected format
        if (!data.dfg || !data.dfg.nodes || !data.dfg.edges) {
          throw new Error('Invalid data format received from the API');
        }

        // Map nodes and edges
        const mappedNodes = data.dfg.nodes.map((node) => ({
          data: { id: node.id, label: node.label || node.id }, // Fallback to `id` if `label` is missing
        }));
        const mappedEdges = data.dfg.edges
          .filter((edge) => edge.source && edge.target) // Only include valid edges
          .map((edge) => ({
            data: {
              source: edge.source.trim(),
              target: edge.target.trim(),
              label: edge.label || '', // Fallback to an empty string if `label` is missing
              weight: edge.count || 0, // Fallback to 0 if `count` is missing
            },
          }));

        // Log the mapped nodes and edges
        console.log('Mapped Nodes:', mappedNodes);
        console.log('Mapped Edges:', mappedEdges);

        // Initialize Cytoscape with the fetched data
        cytoscape({
          container: document.getElementById('cy'), // container to render in
          elements: [...mappedNodes, ...mappedEdges],
          style: [
            {
              selector: 'node[label]', // Apply styles only to nodes with a `label` property
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
                'line-color': 'red', // Change edge line color to red
                'target-arrow-color': 'red', // Change arrow color to red
                'target-arrow-shape': 'triangle',
                'curve-style': 'bezier',
                'label': 'data(label)', // Display edge labels
                'font-size': '10px',
                'text-rotation': 'autorotate',
                'text-margin-y': -10,
              },
            },
          ],
          layout: {
            name: 'dagre', // Use dagre layout for directed graphs
            rankDir: 'LR', // Left-to-right layout
            padding: 10,
          },
        }).on('ready', () => {
          console.log('Cytoscape initialized');
        });
      })
      .catch((error) => {
        console.error('Error fetching graph data:', error);
      });
  }, []);

  return <div id="cy" style={{ width: '100%', height: '600px' }} />;
};

export default Graph;
