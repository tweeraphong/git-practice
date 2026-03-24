from pipeline.extract import extract
from pipeline.transform import transform
from pipeline.validate import validate
from pipeline.load import load
from pipeline.logger import logger


def run_pipeline():
    logger.info("----- Pipeline started -----")
    
    df = extract()
    logger.info("Extract completed")
    
    df = transform(df)
    logger.info("Transform completed")
    
    validate(df)
    
    load(df)
    logger.info("Load completed")
    
    logger.info("----- Pipeline finished -----")

if __name__ == "__main__":
    run_pipeline()