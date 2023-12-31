# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dialogue_pb2 as dialogue__pb2


class CommunicatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.searchContent = channel.unary_unary(
                '/demo.Communicator/searchContent',
                request_serializer=dialogue__pb2.Message.SerializeToString,
                response_deserializer=dialogue__pb2.Content.FromString,
                )
        self.ask = channel.unary_unary(
                '/demo.Communicator/ask',
                request_serializer=dialogue__pb2.Conversation.SerializeToString,
                response_deserializer=dialogue__pb2.Conversation.FromString,
                )
        self.askStreamReply = channel.unary_stream(
                '/demo.Communicator/askStreamReply',
                request_serializer=dialogue__pb2.Conversation.SerializeToString,
                response_deserializer=dialogue__pb2.Message.FromString,
                )
        self.askBidiStream = channel.stream_stream(
                '/demo.Communicator/askBidiStream',
                request_serializer=dialogue__pb2.Conversation.SerializeToString,
                response_deserializer=dialogue__pb2.Conversation.FromString,
                )


class CommunicatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def searchContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def askStreamReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def askBidiStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommunicatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'searchContent': grpc.unary_unary_rpc_method_handler(
                    servicer.searchContent,
                    request_deserializer=dialogue__pb2.Message.FromString,
                    response_serializer=dialogue__pb2.Content.SerializeToString,
            ),
            'ask': grpc.unary_unary_rpc_method_handler(
                    servicer.ask,
                    request_deserializer=dialogue__pb2.Conversation.FromString,
                    response_serializer=dialogue__pb2.Conversation.SerializeToString,
            ),
            'askStreamReply': grpc.unary_stream_rpc_method_handler(
                    servicer.askStreamReply,
                    request_deserializer=dialogue__pb2.Conversation.FromString,
                    response_serializer=dialogue__pb2.Message.SerializeToString,
            ),
            'askBidiStream': grpc.stream_stream_rpc_method_handler(
                    servicer.askBidiStream,
                    request_deserializer=dialogue__pb2.Conversation.FromString,
                    response_serializer=dialogue__pb2.Conversation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'demo.Communicator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Communicator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def searchContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.Communicator/searchContent',
            dialogue__pb2.Message.SerializeToString,
            dialogue__pb2.Content.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/demo.Communicator/ask',
            dialogue__pb2.Conversation.SerializeToString,
            dialogue__pb2.Conversation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def askStreamReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/demo.Communicator/askStreamReply',
            dialogue__pb2.Conversation.SerializeToString,
            dialogue__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def askBidiStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/demo.Communicator/askBidiStream',
            dialogue__pb2.Conversation.SerializeToString,
            dialogue__pb2.Conversation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
