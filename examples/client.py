from __future__ import print_function

import argparse
import json
import logging
import socket

import grpc
from dataset_grpc_server.grpc_files import (
    tiramisu_function_pb2,
    tiramisu_function_pb2_grpc,
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="localhost")
    args = parser.parse_args()
    return args


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to get a tiramisu function from the server ...")
    args = parse_args()
    ip = args.ip

    # ip = socket.gethostbyname(socket.gethostname())
    with grpc.insecure_channel(f"{ip}:50051") as channel:
        stub = tiramisu_function_pb2_grpc.TiramisuDataServerStub(channel)
        response = stub.GetTiramisuFunction(
            tiramisu_function_pb2.TiramisuFunctionName(name="")
        )
    print(response.name, json.loads(response.content).keys(), response.cpp)


if __name__ == "__main__":
    logging.basicConfig()
    run()
