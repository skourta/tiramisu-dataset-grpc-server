import argparse
import json
import logging
import socket
from concurrent import futures
from typing import Dict

import grpc
import grpc_files.tiramisu_function_pb2 as tiramisu_function_pb2
import grpc_files.tiramisu_function_pb2_grpc as tiramisu_function_pb2_grpc
from data_service import DataService

from config import Config


class TiramisuServicer(tiramisu_function_pb2_grpc.TiramisuDataServerServicer):
    def __init__(self) -> None:
        super().__init__()
        if not Config.config:
            Config.init()

        self.data_service = DataService(Config.config)

    def GetTiramisuFunction(self, request, context):
        function_name = request.name
        if function_name != "":
            data, cpp = self.data_service.get_function_by_name(function_name)
        else:
            function_name, data, cpp = self.data_service.get_next_function()
        print("Served", function_name)
        return tiramisu_function_pb2.TiramisuFuction(
            name=function_name, content=json.dumps(data), cpp=json.dumps(cpp)
        )

    def SaveTiramisuFunction(self, request, context):
        function_name = request.name
        data: Dict = json.loads(request.content)
        self.data_service.update_dataset(function_name, data)
        return tiramisu_function_pb2.TiramisuFunctionName(name=function_name)


def serve(port="50051"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tiramisu_function_pb2_grpc.add_TiramisuDataServerServicer_to_server(
        TiramisuServicer(), server
    )
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(
        f"Server started, listening on {socket.gethostbyname(socket.gethostname())}:{port}"
    )
    server.wait_for_termination()


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=str, default="50051")
parser.add_argument("--config", type=str, default="./config.yaml")

if __name__ == "__main__":
    logging.basicConfig()
    args = parser.parse_args()
    Config.init(config_yaml=args.config)
    serve(port=args.port)
