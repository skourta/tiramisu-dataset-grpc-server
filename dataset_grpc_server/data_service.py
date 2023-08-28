import pickle
import random
from typing import Dict, List

from config import DatasetConfig


class DataService:
    def __init__(
        self,
        dataset_config: DatasetConfig,
    ):
        self.dataset_path = dataset_config.dataset_path
        self.cpps_path = dataset_config.cpps_path
        self.path_to_save_dataset = dataset_config.save_path
        self.shuffle = dataset_config.shuffle
        self.seed = dataset_config.seed
        self.saving_frequency = dataset_config.saving_frequency

        self.dataset = {}
        self.function_names: List[str] = []
        self.dataset_size = 0
        self.current_function_index = 0
        self.nbr_updates = 0
        self.dataset_name = dataset_config.dataset_path.split("/")[-1].split(".")[0]
        self.cpps = {}

        print(
            f"reading dataset in full pkl format: dataset pkl from {self.dataset_path} and cpps pkl from {self.cpps_path}"
        )

        with open(self.dataset_path, "rb") as f:
            self.dataset: Dict = pickle.load(f)
            self.function_names = list(self.dataset.keys())

        with open(self.cpps_path, "rb") as f:
            self.cpps: Dict = pickle.load(f)

        # Shuffle the dataset (can be used with random sampling turned off to get a random order)
        if self.shuffle:
            # Set the seed if specified (for reproducibility)
            if self.seed is not None:
                random.seed(self.seed)
            random.shuffle(self.function_names)

        self.dataset_size = len(self.function_names)

    # Returns next function name, function data, and function cpps
    def get_next_function(self, randomize=False):
        if randomize:
            function_name: str = random.choice(self.function_names)
        # Choose the next function sequentially
        else:
            function_name: str = self.function_names[
                self.current_function_index % self.dataset_size
            ]
            self.current_function_index += 1

        return function_name, self.dataset[function_name], self.cpps[function_name]

    def get_function_by_name(self, function_name):
        return self.dataset[function_name], self.cpps[function_name]
