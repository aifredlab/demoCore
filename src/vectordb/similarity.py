from pymilvus import MilvusClient
from vectordb import embedding as embedding       # Document 리턴
import os

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
        limit=5,
        output_fields=["text"]
    )
    print(f"# collection search = {res}")
    print("------------------------------------------\n\n")
    
    return post_process( res );


def post_process(vectortext) :
    textarr = [obj['entity']['text'] for obj in vectortext[0]]
    fulltext = " ".join(textarr)
    fulltext = fulltext.replace("\n", "")

    print(fulltext) 
    return fulltext

# test
# print(  search("계약자가  회사에  보험수익자가  변경되었음을  통지하기  전에") )

