def validate(df, logger):
    logger.info("Starting validation")

    if df["employee_id"].isnull().any():
        raise ValueError("Null employee_id detected")

    if (df["capacity"] < 0).any():
        raise ValueError("Negative capacity detected")

    if (df["planned_hours"] < 0).any():
        raise ValueError("Negative planned_hours detected")

    if (df["actual_hours"] < 0).any():
        raise ValueError("Negative actual_hours detected")

    logger.info("Validation passed")
