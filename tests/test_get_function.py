import json

import grpc
from dataset_grpc_server.grpc_files import (
    tiramisu_function_pb2,
    tiramisu_function_pb2_grpc,
)


def test_get_function():
    with grpc.insecure_channel(f"localhost:50051") as channel:
        stub = tiramisu_function_pb2_grpc.TiramisuDataServerStub(channel)
        response = stub.GetTiramisuFunction(
            tiramisu_function_pb2.TiramisuFunctionName(name="")
        )

    assert response.name != ""
    assert response.name.startswith("function")
    assert type(response.wrapper) == bytes


def test_get_function_by_name():
    with grpc.insecure_channel(f"localhost:50051") as channel:
        stub = tiramisu_function_pb2_grpc.TiramisuDataServerStub(channel)
        response = stub.GetTiramisuFunction(
            tiramisu_function_pb2.TiramisuFunctionName(name="function789281")
        )

    assert response.name == "function789281"
    content = json.loads(response.content)
    assert "program_annotation" in content
    assert type(response.wrapper) == bytes
