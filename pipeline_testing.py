from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.exception import HousingException
import sys

def main():
    try:
        pipe = Pipeline()
        pipe.run_pipeline()

    except Exception as e:
        raise HousingException(e,sys) from e

if __name__=="__main__":
    main()


