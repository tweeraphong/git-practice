from pipeline.logger import logger

def validate(df):
    errors = []
    logger.info("Validation started")

    if df.isnull().sum().sum() > 0:
        errors.append("Null values found")

    if (df["quantity"] <= 0).any():
        errors.append("Invalid quantity detected")


    if (df["price"] <= 0).any():
        errors.append("Invalid price detected")
        
    if df.duplicated().any():
        errors.append("Duplicate records found")

    if errors:
        raise Exception(f"Validation failed: {errors}")
    
    # check variable interger type invalid values
    negative_quantity = (df["quantity"] < 0).sum() 
    if negative_quantity > 0:
        logger.warning(f"{negative_quantity} rows contain negative quantity")
     
    negative_price = (df["price"] <= 0).sum()
    if negative_price > 0:
         logger.warning(f"{negative_price} rows contain negative price")

    logger.info("Validation completed")
    return True