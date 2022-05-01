from collections import namedtuple

DatasetConfig = namedtuple("DatasetConfig", ["name",
                                             "schema",
                                             "batch",
                                             "buffer_size"])

#Validation config has to be added

PreprocessingConfig = namedtuple("PreprocessingConfig", ["vocal_size"])

ModelTrainingConfig = namedtuple("ModelTrainingConfig", ["model_save_dir",
                                                         "model_checkpoint_dir",
                                                         "model_root_dir",
                                                         "epoch",
                                                         "tensorboard_log_dir",
                                                         "base_accuracy",
                                                         "validation_step"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifacts_dir"])