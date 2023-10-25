from concurrent import futures
import logging

import grpc
import ask_pb2 
import ask_pb2_grpc
import dialogue_pb2
import dialogue_pb2_grpc
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import Any
from main import Aifred

class Asker(ask_pb2_grpc.AskerServicer):
    def Ask(self, request, context):
        result = Aifred().process(request.question)
        return ask_pb2.AskReply(**result)

class Communicator(dialogue_pb2_grpc.CommunicatorServicer):

    def searchContent(self, request, context):
        result = Aifred().searchContent(request.text)
        return dialogue_pb2.Content(**result)


    def askStreamReply(self
                       , request: dialogue_pb2.Conversation
                       , context) -> dialogue_pb2.Message:

        ''' 질문에 대한 응답을 스트리밍으로 전달하는 메소드 '''

        # 1. 참고 내용을 가져온다.
        contentMsg = "" #str(doc)
        contentList = request.content
        if (len(contentList) > 0):
            sorted_list = sorted(contentList, key=lambda x: x.time, reverse=True)
            contentMsg = sorted_list[0].content
            contentMsg = contentMsg + "\n 위 내용에 따라 아래 질문에 답변해줘"

        # 2. 질문을 가져온다.
        prompt = request.message.text

        # 3. GPT3를 이용해 답변을 생성한다.
        chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], model_name='gpt-3.5-turbo', temperature=0.9)
        sys = SystemMessage(content=contentMsg)
        msg = HumanMessage(content=prompt)

        # 4. 답변을 전달한다.
        for result in chat.stream([sys, msg]):
            print("### result=", result)
            yield dialogue_pb2.Message(text=result.content)


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
