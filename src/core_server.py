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
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import asyncio
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

    def askStreamReply(self, request, context):
        """ result = Aifred().searchContent(request.message.text)
        message = dialogue_pb2.Message()
        message.text = result

        yield dialogue_pb2.Conversation(message=message) """

        print("### askStreamReply=", request)
        prompt = request.message.text


        #chat = ChatOpenAI(streaming=True, callbacks=[StreamHandler()], model_name='gpt-3.5-turbo', temperature=0.9)
        chat = ChatOpenAI(streaming=True, callbacks=[StreamHandler()], model_name='gpt-3.5-turbo', temperature=0.9)

        contentMsg = "" #str(doc)
        sysMsg = contentMsg + "\n 위 내용에 따라 아래 질문에 답변해줘"
        sys = SystemMessage(content=sysMsg)
        msg = HumanMessage(content=prompt)

        for result in chat.astream(input='오늘 날씨는 어때요?'):
            print("### result=", result)
            yield dialogue_pb2.Message(text=result.content)


class StreamHandler(StreamingStdOutCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        print("overide", token)
        result = dialogue_pb2.Message(text=token)  
        yield result
        


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
