import yaml
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load
from scripts.validation import validate
from scripts.logger import setup_logger

def pipeline():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    logger = setup_logger(config["log_file"])

    logger.info("Pipeline started")
    
    planned, actual, employees = extract(config, logger)

    df = transform(planned, actual, employees, logger)

    validate(df, logger)

    load(df, config, logger)

    logger.info("Pipeline finished")

if __name__ == "__main__":
    pipeline()
