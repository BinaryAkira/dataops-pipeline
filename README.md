# DataOps Pipeline

## Overview

This repository demonstrates a simple data engineering pipeline using Python. It is designed for beginners and shows how raw data can be ingested, transformed, validated, and saved in a structured way.

## What is a Data Pipeline?

A data pipeline is a series of steps that move and process data from one place to another. In this project, the pipeline:
- Loads raw data (e.g., Pokémon information)
- Cleans and transforms the data into a usable format
- Validates the processed data for quality
- Saves the final dataset for further analysis

## Project Structure

- `data/`: Contains raw and processed data files.
  - `raw/`: Where the original data (e.g., JSON files) is stored.
  - `processed/`: Where cleaned and transformed data (e.g., CSV files) is saved.
- `src/`: Source code for the pipeline.
  - `ingest/`: Code to load raw data.
  - `transform/`: Code to clean and reshape the data.
  - `validate/`: Code to check data quality.
  - `utils/`: Helper functions (like logging).
  - `pipeline.py`: Orchestrates the entire pipeline.
- `main.py`: Entry point to run the pipeline.
- `requirements.txt`: Lists Python packages needed.
- `logs/`: Stores logs about pipeline execution.

## How the Pipeline Works

1. **Ingest**: Loads raw data from disk.
2. **Transform**: Cleans and restructures the data (e.g., extracts relevant fields, converts formats).
3. **Validate**: Checks the processed data for errors or inconsistencies.
4. **Save**: Writes the final, clean dataset to disk.

## Setting Up a Virtual Environment (venv)

A virtual environment helps keep your project’s dependencies isolated from other Python projects. Here’s how to create and activate one:

1. Open a terminal or command prompt in your project folder.
2. Create a virtual environment:
   ```
   python -m venv pipeline-venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     pipeline-venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source pipeline-venv/bin/activate
     ```

Once activated, your terminal will show the environment name (e.g., `(pipeline-venv)`). Now you can install packages and run your code safely.

## Getting Started

1. Activate your virtual environment (see above).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   ```
   python main.py
   ```

## Why Use a Pipeline?

- Makes data processing repeatable and reliable.
- Helps organize code and data for easy maintenance.
- Ensures data quality before analysis.
