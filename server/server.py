import time
from concurrent import futures

import grpc

import calculator
from proto import calculator_pb2, calculator_pb2_grpc

ONE_DAY_IN_SECONDS = 60 * 60 * 24


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.val = calculator.square_root(request.val)
        return response


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    print("Starting server...")
    server.add_insecure_port('[::]:80')
    server.start()

    try:
        while True:
            time.sleep(ONE_DAY_IN_SECONDS)

    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()