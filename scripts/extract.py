import pandas as pd

def extract(config, logger):
    try:
        logger.info("Starting extraction")
        
        planned = pd.read_csv(config["input_path"] + "planned.csv")
        actual = pd.read_csv(config["input_path"] + "actual.csv")
        employees = pd.read_csv(config["input_path"] + "employees.csv")

        logger.info("Extraction completed")

        return planned, actual, employees

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise
