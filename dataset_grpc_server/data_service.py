import pickle
import random
from typing import Dict, List

from config import DatasetConfig


class DataService:
    def __init__(self, dataset_config: DatasetConfig, current_function_index: int = 0):
        self.dataset_path = dataset_config.dataset_path
        self.cpps_path = dataset_config.cpps_path
        self.path_to_save_dataset = dataset_config.save_path
        self.shuffle = dataset_config.shuffle
        self.seed = dataset_config.seed
        self.saving_frequency = dataset_config.saving_frequency
        self.wrappers_path = dataset_config.wrappers_path
        self.current_function_index = current_function_index

        self.dataset = {}
        self.function_names: List[str] = []
        self.dataset_size = 0
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

        if self.wrappers_path:
            with open(self.wrappers_path, "rb") as f:
                self.wrappers: Dict = pickle.load(f)

            # intersection of functions in dataset and wrappers
            self.function_names = list(
                set(self.function_names) & set(self.wrappers.keys())
            )

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

        wrapper = self.wrappers[function_name] if self.wrappers_path else None
        return (
            function_name,
            self.dataset[function_name],
            self.cpps[function_name],
            wrapper,
        )

    def get_function_by_name(self, function_name):
        wrapper = self.wrappers[function_name] if self.wrappers_path else None
        return (
            self.dataset[function_name],
            self.cpps[function_name],
            wrapper,
        )

    # Update the dataset with the new function
    def update_dataset(self, function_name: str, function_dict: dict) -> bool:
        """
        Update the dataset with the new function
        :param function_name: name of the function
        :param function_dict: dictionary containing the function schedules
        :return: True if the dataset was saved successfully
        """
        for key in function_dict.keys():
            self.dataset[function_name][key] = function_dict[key]

        self.nbr_updates += 1
        # print(f"# updates: {self.nbr_updates}")
        if self.nbr_updates % self.saving_frequency == 0:
            if self.nbr_updates % (2 * self.saving_frequency):
                return self.save_dataset_to_disk(version=2)
            else:
                return self.save_dataset_to_disk(version=1)
        return False

    # Save the dataset to disk
    def save_dataset_to_disk(self, version=1) -> bool:
        """
        Save the dataset to disk
        :param version: version of the dataset to save (1 or 2)
        :return: True if the dataset was saved successfully
        """
        print("[Start] Save the legality_annotations_dict to disk")

        updated_dataset_name = (
            f"{self.path_to_save_dataset}/{self.dataset_name}_updated_{version}"
        )
        with open(f"{updated_dataset_name}.pkl", "wb") as f:
            pickle.dump(self.dataset, f, protocol=pickle.HIGHEST_PROTOCOL)

        print("[Done] Save the legality_annotations_dict to disk")
        return True
