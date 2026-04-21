def transform (planned, actual, employees, logger):

    try:
        logger.info("Starting tranformation")

        df = planned.merge(
            actual,
            on=["employee_id", "project_id", "date"],
            how="outer")

        df = df.merge(employees, on="employee_id", how="left")
        
        df["planned_hours"] = df["planned_hours"].fillna(0)
        df["actual_hours"] = df["actual_hours"].fillna(0)

        df["capacity"] = 8 * df["fte"]
        df["idle_time"] = (df["capacity"] - df["actual_hours"]).clip(lower=0)

        logger.info("Tranformation completed")

        return df

    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        raise
