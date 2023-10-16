
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


#    if  약관내용 존재 == True:
#        contentMsg = str(doc)
#        sysMsg = contentMsg + "\n\n" \             
#                "\n- 위 내용을 기준으로 아래 질문에 대해 답변할때 필요한 정보를 나열해줘" \
#                "\n- 필요한 정보에 대해서 물어볼수 있는 질문 내용을 만들어줘" \
#                "\n- 예를들어 성별 정보가 필요할 경우 [성별을 알려주세요]라고 말해줘" \
#                "\n- 각 질문들은 앞에 번호를 붙여줘" \
#                "\n- 만약 답변에 필요한 정보가 없다면 [없음] 이라고만 말해줘" \
#                "\n- 오직 질문 목록만 나열해줘 다른말은 하지마"
#
#        if condition:
#            pass
#    else:
#        # 약관내용이 없는 경우
#        content = "관련된 약관내용이 없습니다."
#        answer = chat([msg])


    return result
