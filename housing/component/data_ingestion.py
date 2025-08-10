from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
import os
import pandas as pd
import numpy as np
import sys
from sklearn.model_selection import StratifiedShuffleSplit
from six.moves import urllib



class DataIngestion:
   
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'-'*20}Data Ingestion Started{'-'*20}")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def download_data(self,)->str:
        try:
            # step 1 intilize download url
            download_url = self.data_ingestion_config.dataset_download_url
            # initilize download folder
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            # creating directory 
            os.makedirs(tgz_download_dir,exist_ok=True)
            # extracting file name
            tgz_file_name = os.path.basename(download_url)
            # creating saved file path
            tgz_file_path = os.path.join(tgz_download_dir,
                                     tgz_file_name)
            logging.info(f"Downloading Data From: {download_url} into {tgz_file_path}")
            # downloading DATA
            urllib.request.urlretrieve(download_url,filename=tgz_file_path)
            logging.info(f"{'-'*20}Data Download Completed{'-'*20}")
            #returning download file path
            return tgz_file_path  

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def extract_tgz_data(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracting tgz file: {tgz_file_path} into dir: {raw_data_dir}")
            with tarfile.open(tgz_file_path) as housing_tgz_file_object:
                housing_tgz_file_object.extractall(path = raw_data_dir)
            logging.info(f"Extraction completed")

        except Exception as e:
            raise HousingException(e,sys) from e
 
    def split_data_train_test(self):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            file_name = os.listdir(raw_data_dir)[0]
            file_path = os.path.join(raw_data_dir,file_name)
            
            logging.info(f'reading file:-{[file_path]}')
            housing_data = pd.read_csv(file_path)

            housing_data["income_cat"] = pd.cut(housing_data['median_income'],
                                                bins = [0.0,1.5,3.0,4.5,6.0,np.inf],
                                                labels=[1,2,3,4,5]
                                                )
                       
            split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

            strat_train_data = None
            strat_test_data = None

            for train_index, test_index in split.split(housing_data,housing_data['income_cat']):
                strat_train_data = housing_data.iloc[train_index].drop('income_cat',axis=1)
                strat_test_data = housing_data.iloc[test_index].drop('income_cat',axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)

            if strat_train_data is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir)
                logging.info(f'exporting training data to :- {[train_file_path]}')
                strat_train_data.to_csv(train_file_path)


            if strat_test_data is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir)
                logging.info(f'exporting testing data to :- {[test_file_path]}')
                strat_test_data.to_csv(test_file_path)

            data_ingestion_artifact=DataIngestionArtifact(
                                                train_file_path=train_file_path,
                                                test_file_path=test_file_path,
                                                is_ingested=True,
                                                message="Train and Test File ingested"
                                                )
            logging.info(f'exporting training data to :- {[train_file_path]}')
            logging.info(f'Data Ingestion Artifact :- {[data_ingestion_artifact]}')
            return data_ingestion_artifact



        except Exception as e:
            raise HousingException(e,sys) from e
 
    
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            tgz_file_path = self.download_data()

            self.extract_tgz_data(tgz_file_path=tgz_file_path)
            return self.split_data_train_test()
        
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def __del__(self):
        logging.info(f"{'*'*20}Data Ingestion Log Completed{'*'*20} \n\n")
        

 
        
