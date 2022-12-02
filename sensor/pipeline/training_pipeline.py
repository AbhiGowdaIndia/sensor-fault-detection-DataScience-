from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging


class TrainingPipeline:

    def __init__(self):
        trainig_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=trainig_pipeline_config)

        self.training_pipline_config = trainig_pipeline_config

    def start_data_ingestion(self)->DataIngestionArtifact:
        try :
            logging.info("Staring data ingestion")

            logging.info("Data ingestion completed.")
        except Exception as e:
            raise SensorException(e,sys)

    def start_data_validation(self):
        try :
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_data_tranformation(self):
        try :
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_model_trainer(self):
        try :
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def start_model_evaluation(self):
        try :
            pass
        except Exception as e:
            raise SensorException(e,sys)
   
    def start_model_pusher(self):
        try :
            pass
        except Exception as e:
            raise SensorException(e,sys)

    def run_pipeline(self):
        try :
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)
