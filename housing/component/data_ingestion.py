from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
import os
from six.moves import urllib



class DataIngestion:
   
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'-'*20}Data Ingestion Started{'-'*20}")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise HousingException(e) from e
    
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
            raise HousingException(e) from e
    
    def extract_tgz_data(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracting tgz file: {tgz_file_path} into dir: {raw_data_dir}")
            with tarfile.open(tgz_file_path) as housing_tgz_file_object:
                housing_tgz_file_object.extractall(path = raw_data_dir)
            logging.info(f"{20*'-'}Extraction completed{20*'-'}")

        except Exception as e:
            raise HousingException(e) from e
 
    def split_data_train_test(self):
        try:
            
        except Exception as e:
            raise HousingException(e) from e
 
    
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            tgz_file_path = self.download_data()

            self.extract_tgz_data(tgz_file_path=tgz_file_path)
            
        except Exception as e:
            raise HousingException(e) from e
 
        
