# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import tiramisu_function_pb2 as tiramisu__function__pb2


class TiramisuDataServerStub(object):
    """The greeting service definition."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTiramisuFunction = channel.unary_unary(
            "/tiramisudataserver.TiramisuDataServer/GetTiramisuFunction",
            request_serializer=tiramisu__function__pb2.TiramisuFunctionName.SerializeToString,
            response_deserializer=tiramisu__function__pb2.TiramisuFuction.FromString,
        )


class TiramisuDataServerServicer(object):
    """The greeting service definition."""

    def GetTiramisuFunction(self, request, context):
        """Sends a greeting"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TiramisuDataServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetTiramisuFunction": grpc.unary_unary_rpc_method_handler(
            servicer.GetTiramisuFunction,
            request_deserializer=tiramisu__function__pb2.TiramisuFunctionName.FromString,
            response_serializer=tiramisu__function__pb2.TiramisuFuction.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "tiramisudataserver.TiramisuDataServer", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TiramisuDataServer(object):
    """The greeting service definition."""

    @staticmethod
    def GetTiramisuFunction(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/tiramisudataserver.TiramisuDataServer/GetTiramisuFunction",
            tiramisu__function__pb2.TiramisuFunctionName.SerializeToString,
            tiramisu__function__pb2.TiramisuFuction.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
