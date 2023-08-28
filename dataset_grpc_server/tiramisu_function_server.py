import json
import logging
import pickle
import socket
from concurrent import futures
from typing import Tuple

import grpc
import grpc_files.tiramisu_function_pb2 as tiramisu_function_pb2
import grpc_files.tiramisu_function_pb2_grpc as tiramisu_function_pb2_grpc
from config import Config
from data_service import DataService

# def load_test_data() -> Tuple[dict, dict]:
#     with open("_tmp/test_data.pkl", "rb") as f:
#         dataset = pickle.load(f)
#     with open("_tmp/test_data_cpps.pkl", "rb") as f:
#         cpps = pickle.load(f)
#     return dataset, cpps


class TiramisuServicer(tiramisu_function_pb2_grpc.TiramisuDataServerServicer):
    def __init__(self) -> None:
        super().__init__()
        if not Config.config:
            Config.init()

        self.data_service = DataService(Config.config)
        # self.dataset, self.cpps = load_test_data()
        # self.current_function = 0
        # self.keys = list(self.dataset.keys())

    def GetTiramisuFunction(self, request, context):
        function_name = request.name
        if function_name != "":
            data, cpp = self.data_service.get_function_by_name(function_name)
        else:
            function_name, data, cpp = self.data_service.get_next_function()
            # function_name = self.keys[self.current_function]
            # data = self.dataset[function_name]
            # cpp = self.cpps[function_name]
            # self.current_function += 1
            # if self.current_function >= len(self.keys):
            #     self.current_function = 0
        print(function_name)
        return tiramisu_function_pb2.TiramisuFuction(
            name=function_name, content=json.dumps(data), cpp=json.dumps(cpp)
        )


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tiramisu_function_pb2_grpc.add_TiramisuDataServerServicer_to_server(
        TiramisuServicer(), server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(
        f"Server started, listening on {socket.gethostbyname(socket.gethostname())}:{port}"
    )
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
