from Network_security.components.data_ingestion import DataIngestion
from Network_security.exception.exception import NetworkSecurityException
from Network_security.logging.logger import logging
import sys
from Network_security.entity.config_entity import DataIngestionConfig
from Network_security.entity.artifact_entity import DataIngestionArtifact
from Network_security.entity.config_entity import TrainingPipelineConfig


if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Initiate data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
        