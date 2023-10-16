from pymilvus import MilvusClient
from vectordb import embedding as embedding       # Document 리턴
import os
import re

# replace
def search(prompt):
    client = MilvusClient(
        uri=os.environ.get('ZILLIZ_CLOUD_URI'),
        token=os.environ.get('ZILLIZ_CLOUD_API_KEY')
    )

    vector_data = embedding.embedding_openai(prompt)
    #print(f"##################={len(vector_data)}")

    res = client.search(
        collection_name=os.environ.get('COLLECTION_NAME'),
        data=[ vector_data ],
        limit=1,
        output_fields=["text"]
    )
    print(f"# collection search = {res}")
    print("------------------------------------------\n\n")
    
    return post_process( res );


def post_process(vectortext) :
    # text 부분 추출하여 array로 생성하고 array를 하나의 text로 합침
    textarr = [obj['entity']['text'] for obj in vectortext[0]]
    fulltext = " ".join(textarr)
    
    # 쓸데없는 띄어쓰기 삭제
    # fulltext = fulltext.replace("\n", "")
    
    # http 주소 삭제
    fulltext = remove_http_urls(fulltext)
    
    print(fulltext) 
    return fulltext

def remove_http_urls(text):
    # 정규 표현식 패턴: http:// 또는 https://로 시작하고, 공백이나 문자열 끝으로 끝나는 부분을 찾습니다.
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    # 패턴과 일치하는 부분을 빈 문자열로 대체합니다.
    return url_pattern.sub('', text)

# test
# print(  search("계약자가  회사에  보험수익자가  변경되었음을  통지하기  전에") )

