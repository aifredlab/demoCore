
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def main(doc, prompt):
    chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)
    
    contentMsg = str(doc)
    sysMsg = contentMsg + "\n 위 내용에 따라 아래 질문에 답변해줘"
    sys = SystemMessage(content=sysMsg)
    msg = HumanMessage(content=prompt)

    answer = ""
    chat_result = chat([sys, msg])
    if chat_result is not None:
        answer = chat_result.content

    result = {}
    result["content"] = contentMsg
    result["answer"] = answer

    return result
