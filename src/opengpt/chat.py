
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def main(doc, prompt):
    chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)

    sysMsg = str(doc)
    sysMsg = sysMsg + "\n 위 내용에 따라 아래 질문에 답변해줘"
    sys = SystemMessage(content=sysMsg)
    msg = HumanMessage(content=prompt)

    result = chat([sys, msg])

    return result
