from affirm.grpc.fixtures.v1 import interface_pb2
from google.protobuf import descriptor_pool

print("\n--- Using descriptor_pool.Default().FindMethodByName ---")
full_method_name_to_find = 'affirm.grpc.fixtures.v1.GrpcTestService.ReflectReqId'
method_descriptor_from_pool = descriptor_pool.Default().FindFileByName("message")

if method_descriptor_from_pool:
    print(f"Found method: {method_descriptor_from_pool.full_name}")
    print(f"  Input type: {method_descriptor_from_pool.input_type.full_name}")
    print(f"  Output type: {method_descriptor_from_pool.output_type.full_name}")
else:
    print(f"Method '{full_method_name_to_find}' not found in descriptor pool.")