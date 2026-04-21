# Pipeline Scripts

## Overview
This folder contains the core logic of the data pipeline.

## Modules

### extract.py
Loads raw data from source files.

### transform.py
- merges datasets
- calculates idle time

### validation.py
Performs data quality checks:
- missing values
- negative values
- schema validation

### load.py
Saves processed data to target storage.

### logger.py
Initialize logging for pipeline execution.

## Design Approach
- modular architecture
- separation of concerns
- reusable components
