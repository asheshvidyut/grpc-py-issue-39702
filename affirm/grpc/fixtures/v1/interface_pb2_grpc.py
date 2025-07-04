# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from affirm.grpc.fixtures.v1 import messages_pb2 as affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in affirm/grpc/fixtures/v1/interface_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GrpcTestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReflectReqId = channel.unary_unary(
                '/affirm.grpc.fixtures.v1.GrpcTestService/ReflectReqId',
                request_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ReflectReqIdRequest.SerializeToString,
                response_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ReflectReqIdResponse.FromString,
                _registered_method=True)
        self.RaiseError = channel.unary_unary(
                '/affirm.grpc.fixtures.v1.GrpcTestService/RaiseError',
                request_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.RaiseErrorRequest.SerializeToString,
                response_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.RaiseErrorResponse.FromString,
                _registered_method=True)
        self.Blocking = channel.unary_unary(
                '/affirm.grpc.fixtures.v1.GrpcTestService/Blocking',
                request_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingRequest.SerializeToString,
                response_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingResponse.FromString,
                _registered_method=True)
        self.BlockingV2 = channel.unary_unary(
                '/affirm.grpc.fixtures.v1.GrpcTestService/BlockingV2',
                request_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingV2Request.SerializeToString,
                response_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingV2Response.FromString,
                _registered_method=True)
        self.Validate = channel.unary_unary(
                '/affirm.grpc.fixtures.v1.GrpcTestService/Validate',
                request_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ValidateRequest.SerializeToString,
                response_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ValidateResponse.FromString,
                _registered_method=True)


class GrpcTestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReflectReqId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RaiseError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Blocking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BlockingV2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Validate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcTestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReflectReqId': grpc.unary_unary_rpc_method_handler(
                    servicer.ReflectReqId,
                    request_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ReflectReqIdRequest.FromString,
                    response_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ReflectReqIdResponse.SerializeToString,
            ),
            'RaiseError': grpc.unary_unary_rpc_method_handler(
                    servicer.RaiseError,
                    request_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.RaiseErrorRequest.FromString,
                    response_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.RaiseErrorResponse.SerializeToString,
            ),
            'Blocking': grpc.unary_unary_rpc_method_handler(
                    servicer.Blocking,
                    request_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingRequest.FromString,
                    response_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingResponse.SerializeToString,
            ),
            'BlockingV2': grpc.unary_unary_rpc_method_handler(
                    servicer.BlockingV2,
                    request_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingV2Request.FromString,
                    response_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingV2Response.SerializeToString,
            ),
            'Validate': grpc.unary_unary_rpc_method_handler(
                    servicer.Validate,
                    request_deserializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ValidateRequest.FromString,
                    response_serializer=affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ValidateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'affirm.grpc.fixtures.v1.GrpcTestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('affirm.grpc.fixtures.v1.GrpcTestService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GrpcTestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReflectReqId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/affirm.grpc.fixtures.v1.GrpcTestService/ReflectReqId',
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ReflectReqIdRequest.SerializeToString,
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ReflectReqIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RaiseError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/affirm.grpc.fixtures.v1.GrpcTestService/RaiseError',
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.RaiseErrorRequest.SerializeToString,
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.RaiseErrorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Blocking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/affirm.grpc.fixtures.v1.GrpcTestService/Blocking',
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingRequest.SerializeToString,
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BlockingV2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/affirm.grpc.fixtures.v1.GrpcTestService/BlockingV2',
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingV2Request.SerializeToString,
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.BlockingV2Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Validate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/affirm.grpc.fixtures.v1.GrpcTestService/Validate',
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ValidateRequest.SerializeToString,
            affirm_dot_grpc_dot_fixtures_dot_v1_dot_messages__pb2.ValidateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
