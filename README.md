# Experimental Data Explorer

## Overview

**Experimental Data Explorer** is a web application for uploading, processing, and visualizing experimental data and questionnaires.  
It consists of a FastAPI backend and a React frontend, both containerized with Docker.

---

## Features

- Upload CSV files and convert them to XES format
- Generate and visualize Directly-Follows Graphs (DFG) from event logs
- Upload and view questionnaire data
- Interactive data exploration interface
- Modern React frontend with Cytoscape.js graph visualization

---

## Project Structure

```
Experimental-Data-Explorer/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── scripts/
│   │       ├── csv_to_xes.py
│   │       ├── process_qst.py
│   │       └── xes_dfg.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   └── .gitignore
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   │       ├── FileUploader.jsx
│   │       ├── Graph.jsx
│   │       ├── Dropdown.jsx
│   │       ├── QstDropdown.jsx
│   │       └── Questionnaire.jsx
│   ├── package.json
│   ├── Dockerfile
│   ├── .dockerignore
│   └── .gitignore
│
├── docker-compose.yml
└── README.md
```

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) and Docker Compose

### Running the Application

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd Experimental-Data-Explorer
   ```

2. **Build and start the services:**

   ```sh
   docker compose up --build
   ```

3. **Access the application:**
   - Frontend: [http://localhost](http://localhost)
   - Backend API: [http://localhost:8000/docs](http://localhost:8000/docs) (FastAPI docs)

---

## Usage

1. **Upload a CSV file** using the interface.
2. The backend processes the file, generates XES and DFG representations, and stores them.
3. Select a file from the dropdown to visualize its Directly-Follows Graph.
4. Upload and view questionnaire data in an interactive format.

---

## Development

### Backend

- FastAPI app in `backend/app/main.py`
- Custom processing scripts in `backend/app/scripts/`
- Install dependencies with:
  ```sh
  pip install -r requirements.txt
  ```

### Frontend

- React app in `frontend/src/`
- Main entry: `frontend/src/App.jsx`
- Install dependencies with:
  ```sh
  npm install
  npm run dev
  ```

---

## Docker

- **Backend**: Python 3.11, FastAPI, Uvicorn
- **Frontend**: Node 20, React, Vite, served with Nginx
- **Compose**: See [`docker-compose.yml`](docker-compose.yml) for service definitions

---

## File Uploads and Data

- Uploaded and processed files are stored in `backend/data/`
- DFG JSON files: `backend/data/dfg_json/`
- Questionnaire JSON files: `backend/data/qst_json/`
- XES files: `backend/data/xes/`
- Uploads: `backend/data/uploads/`

---

## License

MIT License

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)
- [Cytoscape.js](https://js.cytoscape.org/)
- [pm4py](https://pm4py.fit.fraunhofer.de/)

---
