import argparse
import json
import logging
import os
import re
import socket
from concurrent import futures
from typing import Dict

import grpc
import grpc_files.tiramisu_function_pb2 as tiramisu_function_pb2
import grpc_files.tiramisu_function_pb2_grpc as tiramisu_function_pb2_grpc
from data_service import DataService

from config import Config


class TiramisuServicer(tiramisu_function_pb2_grpc.TiramisuDataServerServicer):
    def __init__(self, ip: str, port: int, current_function_index=0) -> None:
        super().__init__()
        if not Config.config:
            Config.init()

        self.ip = ip
        self.port = port

        self.data_service = DataService(
            Config.config, current_function_index=current_function_index
        )

    def GetTiramisuFunction(self, request, context):
        server_file_template = (
            """{ip_and_port}\nlast_function_served:{{{last_function_served_index}}}"""
        )

        function_name = request.name
        if function_name != "":
            data, cpp, wrapper = self.data_service.get_function_by_name(function_name)
        else:
            function_name, data, cpp, wrapper = self.data_service.get_next_function()

        print("Served", function_name)
        # replace the file of the server address with the new one
        with open(
            os.path.join(Config.config.server_address, "server_address"), "w"
        ) as f:
            f.write(
                server_file_template.format(
                    ip_and_port=f"{self.ip}:{self.port}",
                    last_function_served_index=self.data_service.current_function_index
                    - 1,
                )
            )

        return tiramisu_function_pb2.TiramisuFunction(
            name=function_name,
            content=json.dumps(data),
            cpp=json.dumps(cpp),
            wrapper=wrapper,
        )

    def SaveTiramisuFunction(self, request, context):
        function_name = request.name
        data: Dict = json.loads(request.content)
        self.data_service.update_dataset(function_name, data)
        return tiramisu_function_pb2.TiramisuFunctionName(name=function_name)

    def GetDatasetSize(self, request, context):
        return tiramisu_function_pb2.DatasetSize(
            size=len(self.data_service.function_names)
        )

    def GetListOfFunctions(self, request, context):
        return tiramisu_function_pb2.TiramisuListOfFunctions(
            names=self.data_service.function_names
        )


def serve(port="50051", current_function_index=0):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ip = socket.gethostbyname(socket.gethostname())
    port = int(port)
    tiramisu_function_pb2_grpc.add_TiramisuDataServerServicer_to_server(
        TiramisuServicer(ip, port, current_function_index), server
    )
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(
        f"Server started, listening on {ip}:{port}.\nCurrent function index: {current_function_index}"
    )
    with open(os.path.join(Config.config.server_address, "server_address"), "w") as f:
        f.write(f"{ip}:{port}\nlast_function_served:{{{current_function_index-1}}}")

    server.wait_for_termination()


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=str, default="50051")
parser.add_argument("--config", type=str, default="./config.yaml")
# path to save ip and port to
parser.add_argument("--server-address", type=str, default="")
# add boolean flag reset to reset the server address
parser.add_argument("--reset", action="store_true")
parser.add_argument


if __name__ == "__main__":
    logging.basicConfig()
    args = parser.parse_args()

    # load config
    Config.init(config_yaml=args.config)

    # set server address
    if args.server_address:
        Config.config.server_address = args.server_address

    if args.reset:
        current_function_index = 0
    else:
        # read and empty the address file
        with open(
            os.path.join(Config.config.server_address, "server_address"), "r"
        ) as f:
            address_content = f.read()

        # use this regex to get the index of the last function served last_function_served:\{-?(\d+)\}
        last_function_served_regex = r"last_function_served:\{-?(\d+)\}"
        matched = re.search(last_function_served_regex, address_content)
        current_function_index = 0 if not matched else int(matched.group(1)) + 1

    with open(os.path.join(Config.config.server_address, "server_address"), "w") as f:
        f.write("")

    # start the server
    serve(port=args.port, current_function_index=current_function_index)
