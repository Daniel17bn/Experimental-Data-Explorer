# Experimental Data Explorer

## Overview

BSP-1 is a web application for uploading, processing, and visualizing experimental data and questionnaires. It consists of a FastAPI backend and a React frontend.

## Features

- Upload CSV files and convert them to XES format
- Generate and visualize Directly-Follows Graphs (DFG)
- Upload and view questionnaire data
- Interactive data exploration interface

## Project Structure

```
backend/
  app/
    main.py
    scripts/
      csv_to_xes.py
      process_qst.py
      xes_dfg.py
  requirements.txt
frontend/
  src/
    App.jsx
    components/
      FileUploader.jsx
      Graph.jsx
      Dropdown.jsx
      QstDropdown.jsx
      Questionnaire.jsx
  package.json
```
