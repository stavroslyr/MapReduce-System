# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import worker_pb2 as worker__pb2


class WorkerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AssignTask = channel.unary_unary(
                '/worker.Worker/AssignTask',
                request_serializer=worker__pb2.Task.SerializeToString,
                response_deserializer=worker__pb2.Status.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/worker.Worker/GetStatus',
                request_serializer=worker__pb2.Empty.SerializeToString,
                response_deserializer=worker__pb2.Status.FromString,
                )


class WorkerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AssignTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AssignTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignTask,
                    request_deserializer=worker__pb2.Task.FromString,
                    response_serializer=worker__pb2.Status.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=worker__pb2.Empty.FromString,
                    response_serializer=worker__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'worker.Worker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Worker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AssignTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.Worker/AssignTask',
            worker__pb2.Task.SerializeToString,
            worker__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/worker.Worker/GetStatus',
            worker__pb2.Empty.SerializeToString,
            worker__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
