import React from 'react';
import FileUploader from './components/FileUploader';
import Graph from './components/Graph';

function App() {
    return (
        <>
            <h1>BSP Project</h1>
            <div>
                <FileUploader />
            </div>
            <div style={{ marginTop: '2rem' }}>
                <h2>Graph Visualization</h2>
                <Graph />
            </div>
        </>
    );
}

export default App;
