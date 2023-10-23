from dataclasses import dataclass
from typing import Any, Dict

import yaml


@dataclass
class DatasetConfig:
    # dataset_format: DatasetFormat = DatasetFormat.HYBRID
    cpps_path: str = ""
    dataset_path: str = ""
    save_path: str = ""
    shuffle: bool = False
    seed: int = None
    saving_frequency: int = 10000
    server_address: str = "."
    wrappers_path: str | None = None

    def __init__(self, dataset_config_dict: Dict):
        # self.dataset_format = DatasetFormat.from_string(
        #     dataset_config_dict["dataset_format"]
        # )
        self.cpps_path = dataset_config_dict["cpps_path"]
        self.dataset_path = dataset_config_dict["dataset_path"]
        self.save_path = dataset_config_dict["save_path"]
        self.shuffle = dataset_config_dict["shuffle"]
        self.seed = dataset_config_dict["seed"]
        self.saving_frequency = dataset_config_dict["saving_frequency"]

        if "wrappers_path" in dataset_config_dict:
            self.wrappers_path = dataset_config_dict["wrappers_path"]

        if dataset_config_dict["is_benchmark"]:
            self.dataset_path = (
                dataset_config_dict["benchmark_dataset_path"]
                if dataset_config_dict["benchmark_dataset_path"]
                else self.dataset_path
            )
            self.cpps_path = (
                dataset_config_dict["benchmark_cpp_files"]
                if dataset_config_dict["benchmark_cpp_files"]
                else self.cpps_path
            )


def read_yaml_file(path):
    with open(path) as yaml_file:
        return yaml_file.read()


def parse_yaml_file(yaml_string: str):
    return yaml.safe_load(yaml_string)


def dict_to_config(parsed_yaml: Dict[Any, Any]):
    return DatasetConfig(parsed_yaml)


class Config(object):
    config = None

    @classmethod
    def init(self, config_yaml="./config.yaml"):
        parsed_yaml_dict = parse_yaml_file(read_yaml_file(config_yaml))
        Config.config = dict_to_config(parsed_yaml_dict)
