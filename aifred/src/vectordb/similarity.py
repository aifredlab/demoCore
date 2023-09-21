from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus

def main(prompt):
    # FIXME :: 컬랙션부분이나 문서 구분에 대한구분 정의필요함
    m = Milvus(
        OpenAIEmbeddings(),
        #"컬랙션",
        connection_args={"host": "127.0.0.1", "port": "19530"}
    )
    
    docs = m.similarity_search(prompt)

    return docs

