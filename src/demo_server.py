
from concurrent import futures
import logging

import grpc
import ask_pb2 
import ask_pb2_grpc
import os

from main import Aifred

class Asker(ask_pb2_grpc.AskerServicer):
    def Ask(self, request, context):
        result = Aifred().process(request.question)
        return ask_pb2.AskReply(**result)

def serve():
    port = os.environ.get('SERVER_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ask_pb2_grpc.add_AskerServicer_to_server(Asker(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
