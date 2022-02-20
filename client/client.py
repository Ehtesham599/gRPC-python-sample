import grpc
from proto import calculator_pb2, calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:80')

stub = calculator_pb2_grpc.CalculatorStub(channel)

number = calculator_pb2.Number(val=16)
response = stub.SquareRoot(number)
print(response.val)