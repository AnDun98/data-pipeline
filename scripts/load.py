import os

def load(df, config, logger):
    try:
        logger.info("Starting load")

        output_path = config["output_path"]
        os.makedirs(output_path, exist_ok=True)

        file_path = output_path + "workload.csv"

        df.to_csv(file_path, index=False)

        logger.info(f"Data saved to {file_path}")

    except Exception as e:
        logger.error(f"Load failed: {e}")
        raise
