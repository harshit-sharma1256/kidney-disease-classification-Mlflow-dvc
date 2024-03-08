from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)  #This means i don't want to add anything else here.It will throw an error if used try to add something here.
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path      # training folder path
    trained_model_path: Path  # trained model would be saved here
    updated_base_model_path: Path  # NN used for training
    training_data: Path  # dataset used for training
    params_epochs: int    # Number of epochs 
    params_batch_size: int # Batch size during training
    params_is_augmentation: bool
    params_image_size: list   #Input image size