#### To generate the protos

```bash
cd grpc-py-issue-39702
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. affirm/grpc/fixtures/v1/interface.proto affirm/grpc/fixtures/v1/messages.proto
```

#### Run

```bash
(venv) asheshvidyut@asheshvidyut:~/issue-39702$ python test.py

--- Using descriptor_pool.Default().FindMethodByName ---
Found method: affirm.grpc.fixtures.v1.GrpcTestService.ReflectReqId
  Input type: affirm.grpc.fixtures.v1.ReflectReqIdRequest
  Output type: affirm.grpc.fixtures.v1.ReflectReqIdResponse
(venv) asheshvidyut@asheshvidyut:~/issue-39702$
```