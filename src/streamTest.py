from concurrent import futures
import logging
import grpc
import dialogue_pb2
import dialogue_pb2_grpc
import ask_pb2 
import ask_pb2_grpc
import time
from main import Aifred


class Communicator(dialogue_pb2_grpc.CommunicatorServicer):
    def askStreamReply(self, request, context):
        for i in range(1, 11):
            message = {}
            #message["content"] = ''
            message["text"] = "Message {}".format(i)
            print(message["text"])
            
            response = dialogue_pb2.Conversation(message=message)
            yield response
            time.sleep(1)
        
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    
    dialogue_pb2_grpc.add_CommunicatorServicer_to_server(Communicator(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()