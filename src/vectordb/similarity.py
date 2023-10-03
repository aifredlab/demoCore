from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader

# replace
ZILLIZ_CLOUD_URI = "https://in03-bfa4469b6404aa3.api.gcp-us-west1.zillizcloud.com"  # example: "https://in01-17f69c292d4a5sa.aws-us-west-2.vectordb.zillizcloud.com:19536"
ZILLIZ_CLOUD_USERNAME = ""  # example: "username"
ZILLIZ_CLOUD_PASSWORD = ""  # example: "*********"
ZILLIZ_CLOUD_API_KEY = "a3d25208a17af9679b40440b61aeee5c9ad11db43e49d21761f65c5034d2637dda67a4ddf1833bba3ea2c68900c2d169b34e2a8f"  # example: "*********" (for serverless clusters which can be used as replacements for user and password)

def search(prompt):
    # FIXME :: 컬랙션부분이나 문서 구분에 대한구분 정의필요함

    # -------------------------------------
    # connect local server
    # -------------------------------------
#    m = Milvus(
#        OpenAIEmbeddings(),
#        #"컬랙션",
#        connection_args={"host": "127.0.0.1", "port": "19530"}
#    )

    # -------------------------------------
    # connect cloud milvus server (https://cloud.zilliz.com)
    # -------------------------------------
    loader = PyPDFLoader("../doc/samsung_tooth_terms.pdf")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    m = Milvus.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(),
        connection_args={
            "uri": ZILLIZ_CLOUD_URI,
            #"user": ZILLIZ_CLOUD_USERNAME,
            #"password": ZILLIZ_CLOUD_PASSWORD,
            "token": ZILLIZ_CLOUD_API_KEY,  # API key, for serverless clusters which can be used as replacements for user and password
            "secure": True,
        },
    )

    docs = m.similarity_search(prompt)

    return docs

