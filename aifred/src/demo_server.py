from concurrent import futures
import logging

import grpc
import ask_pb2 
import ask_pb2_grpc

class Asker(ask_pb2_grpc.AskerServicer):
    def Ask(self, request, context):

        
        return ask_pb2.AskReply(content="당신의 질문은 [%s]" % request.question)

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ask_pb2_grpc.add_AskerServicer_to_server(Asker(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()
