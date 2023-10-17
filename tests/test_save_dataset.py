import json
import os

import grpc
from dataset_grpc_server.config import Config
from dataset_grpc_server.grpc_files import (
    tiramisu_function_pb2,
    tiramisu_function_pb2_grpc,
)

# def test_get_function_by_name():
#     Config.init()

#     with grpc.insecure_channel(f"localhost:50051") as channel:
#         stub = tiramisu_function_pb2_grpc.TiramisuDataServerStub(channel)
#         response = stub.GetTiramisuFunction(
#             tiramisu_function_pb2.TiramisuFunctionName(name="function789281")
#         )

#         assert response.name == "function789281"
#         content = json.loads(response.content)
#         assert "program_annotation" in content

#         for i in range(Config.config.saving_frequency + 1):
#             save_response = stub.SaveTiramisuFunction(
#                 tiramisu_function_pb2.TiramisuFunction(
#                     name=response.name,
#                     content=json.dumps(content),
#                 )
#             )

#     # check if the datasets folder is not empty
#     assert len(os.listdir(Config.config.save_path)) > 0
