
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

async def chat_with_bot():
    # ChatOpenAI 객체 생성
    chat = ChatOpenAI(
        model_name='gpt-3.5-turbo',
        temperature=0.7,
        max_tokens=50,
        callbacks=[StreamingStdOutCallbackHandler()],
        streaming=True  # 비동기 스트리밍 활성화
    )

    # 대화 시작
    async for response in chat.astream([
        SystemMessage(content="안녕하세요, 챗봇입니다. 무엇을 도와드릴까요?"),
        HumanMessage(content="챗봇에게 날씨 정보를 알려줘.")
    ]):
        print(response.content)  # 챗봇의 응답을 출력
        # yield response.content

if __name__ == "__main__":
    # 환경변수 셋팅
    load_dotenv(dotenv_path='../src/.env')
    asyncio.run(chat_with_bot())
