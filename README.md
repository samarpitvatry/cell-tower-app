
# Cell Tower App

## Introduction
The Cell Tower Dashboard is a Python-based application designed to provide insights into cell tower distributions and densities in the UK. It utilizes data from two CSV files to analyze and visualize cell tower information.

## Prerequisites
Before installing and running the app, ensure you have the following:
- Python 3.x
- Docker (optional, for containerized deployment)

## Installation
1. Clone the repository to your local machine.
2. Install the required Python dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
- To run the app directly:
  ```
  python app.py
  ```
- To run the app as a Docker container:
  ```
  docker build -t cell_tower_app .
  docker run -p 5000:5000 cell_tower_app
  ```

## Files Description
- `app.py`: The main Python script for the app.
- `Dockerfile`: Instructions for building a Docker container for the app.
- `requirements.txt`: A list of Python dependencies.
- `UK_Cell_Tower_Combined.csv`: Dataset containing combined information about UK cell towers.
- `UK_Cell_Tower_Density.csv`: Dataset containing information about the density of cell towers in the UK.

## Contributing
Feel free to contribute to the development of this app by submitting pull requests or opening issues for any bugs or feature requests.
