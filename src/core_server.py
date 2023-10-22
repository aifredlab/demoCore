from concurrent import futures
import logging

import grpc
import ask_pb2 
import ask_pb2_grpc
import dialogue_pb2
import dialogue_pb2_grpc
import os

from main import Aifred

class Asker(ask_pb2_grpc.AskerServicer):
    def Ask(self, request, context):
        result = Aifred().process(request.question)
        return ask_pb2.AskReply(**result)

class Communicator(dialogue_pb2_grpc.CommunicatorServicer):
    def searchContent(self, request, context):
        result = Aifred().searchContent(request.text)
        return dialogue_pb2.Content(**result)

    def askStreamReply(self, request, context):
        result = Aifred().searchContent(request.message.text)
        conversation = dialogue_pb2.Conversation()
        conversation.message.text = result

        return dialogue_pb2.Conversation(**conversation)


def serve():
    port = os.environ.get('SERVER_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # add service
    ask_pb2_grpc.add_AskerServicer_to_server(Asker(), server)
    dialogue_pb2_grpc.add_CommunicatorServicer_to_server(Communicator(), server)

    # start server
    server.add_insecure_port("[::]:" + port) # 인증없이 사용할 수 있도록 설정, 운영환경에서는 add_secure_port를 사용해야 함
    server.start()
    print(f"Server started, listening {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
