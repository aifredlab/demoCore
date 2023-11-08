
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

from dotenv import load_dotenv

# 환경변수 셋팅
load_dotenv(dotenv_path='../src/.env')




def callChatOpenai(chat, systemMessage, prompt):
    # 질문을 가져온다.

    # GPT3를 이용해 답변을 생성한다.
    sys = SystemMessage(content=systemMessage)
    msg = HumanMessage(content=prompt)

    result = chat([sys, msg])
    print(result)




def getChunksFromFile(filename, chunk_size=2000):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    return chunks
    

    # text_arr
    # for i in range(0, len(content), chunk_size):
    #     print(content[i:i + chunk_size])
    #     print('-' * 50)  # 구분선 추가

    # 사용 예
    # filename = 'example.txt'
    # print_chunks(filename)

def makeBatchMessage(text_arr):
    batch_message = []

    # 첫 지침을 전송
    notice = getTemplate(0, len(text_arr), "")
    batch_message.append([
        SystemMessage(content=notice), HumanMessage(content="")
    ])

    # 각 chunk를 처리
    for idx, chunk in enumerate(text_arr, 1):
        context = getTemplate(idx, len(text_arr), chunk)

        if idx == len(text_arr):
            # prompt = "지금까지 입력한 context(SystemMessage)에 대해서 문장을 정리하고 문단별로 나누어줘"
            prompt = "입력된 context를 정리해줘"
        else:
            prompt = ""

        batch_message.append([
            SystemMessage(content=context), HumanMessage(content=prompt)
        ])

    return batch_message


def getTemplate(current, total, text):

    if current == 0:
        text = f"""
        The total length of the content that I want to send you is too large to send in only one piece.
        For sending you that content, I will follow this rule:
                
        [START PART {current}/{total}]
        this is the content of the part {current} out of {total} in total
        [END PART {current}/{total}]
                
        Then you just answer: "Received part {current}/{total}"
        And when I tell you "ALL PARTS SENT", then you can continue processing the data and answering my requests.
        """
    elif current == total:
        text = f"""
        [START PART {current}/{total}]
        {text}
        [END PART {current}/{total}]
        ALL PARTS SENT. Now you can continue processing the request.
        """

    else:
        text = f"""
        Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part {current}/{total} received" and wait for the next part.
        [START PART {current}/{total}]
        {text}
        [END PART {current}/{total}]
        Remember not answering yet. Just acknowledge you received this part with the message "Part {current}/{total} received" and wait for the next part.
        """

    return text



# GPT3 모델 생성
chat = ChatOpenAI(streaming=False, model_name='gpt-3.5-turbo', temperature=0.9)

text_arr = getChunksFromFile('../doc/sample_extract_pdf.txt')
# batch_messages = makeBatchMessage(text_arr)
# result = chat.generate(batch_messages)
# print(result)

order_msg = """입력된 context를 내용의 손실 없이 정리해줘
- 작업한 내용에 대해서 설명하지마
- 내용의 손실없이 정리해줘"""

# 각 chunk를 처리
for idx, chunk in enumerate(text_arr, 1):
    # prompt = getTemplate(idx, len(text_arr), chunk)
    callChatOpenai(chat, chunk, order_msg)


# 파일 읽기
# with open('../doc/sample_extract_pdf_part.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     # print(text)
#     callChatOpenai(chat, text, order_msg)


'''
# 첫 지침을 전송
notice = getTemplate(0, len(text_arr), "")
callChatOpenai(chat, notice, "")

# 각 chunk를 처리
for idx, chunk in enumerate(text_arr, 1):
    prompt = getTemplate(idx, len(text_arr), chunk)
    callChatOpenai(chat, "", prompt)
    


# 마지막 질문을 전송
prompt = "임플란트를 보상받기 위해서 가입일로부터 몇일이 지나야 하나요?"
callChatOpenai(chat, "", prompt)
'''





# llm = OpenAI()
# chat_model = ChatOpenAI()
# 
# print(llm.predict("hi!"))
# 
# print(chat_model.predict("hi!"))
