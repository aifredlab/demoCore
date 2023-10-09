from concurrent import futures
import logging

import grpc
import ask_pb2 
import ask_pb2_grpc

from main import Aifred

class Asker(ask_pb2_grpc.AskerServicer):
    def Ask(self, request, context):
        result = Aifred.process(request.question)
        #aifred_instance = Aifred()  # Aifred 클래스의 인스턴스 생성
        #aifred_instance.process("이 상품을 가입해서 만기가 되면 보험료 전액 환급이 가능해?")  # process 메서드 호출
        print("### GRPC Return Data : {result}")
        return ask_pb2.AskReply(content="당신의 질문은 [{result}]")

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
