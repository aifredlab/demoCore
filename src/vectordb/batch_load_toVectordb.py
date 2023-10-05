from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Milvus
from pymilvus import MilvusClient
#from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
import os

ZILLIZ_CLOUD_URI = "https://in03-bfa4469b6404aa3.api.gcp-us-west1.zillizcloud.com"
ZILLIZ_CLOUD_USERNAME = ""
ZILLIZ_CLOUD_PASSWORD = ""
ZILLIZ_CLOUD_API_KEY = "a3d25208a17af9679b40440b61aeee5c9ad11db43e49d21761f65c5034d2637dda67a4ddf1833bba3ea2c68900c2d169b34e2a8f" 
COLLECTION_NAME = "LangChainCollection"

OPENAI_API_KEY = "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" #@param {type:"string"}
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def loadPdf(file_path):
    # -------------------------------------
    # pdf 파일을 읽어서 chunk_size 단위로 배열로 만든다 
    # -------------------------------------
    loader = PyPDFLoader(file_path) # ex: "../doc/samsung_tooth_terms.pdf"
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs_list = text_splitter.split_documents(documents)

    # print (docs_list)
    # ex : Document(page_content='본 약관은 100% 재생펄프를 사용하여 제작한 친환경 인쇄물입니다. 장기상품개발팀 인쇄', metadata={'source': '../doc/samsung_tooth_terms.pdf', 'page': 153})

    # -------------------------------------
    # insert vector_db
    # -------------------------------------

    # - pymilvus를 사용해 vector를 저장하는 방법
    # client = MilvusClient(
    #     uri=ZILLIZ_CLOUD_URI,
    #     token=ZILLIZ_CLOUD_API_KEY, # for serverless clusters, or
    # )
    # 
    # client.insert(collection_name=COLLECTION_NAME, data=docs_list)


    # langchain api를 사용해 vector를 저장하는 방법:
    m = Milvus.from_documents(
        documents=docs_list,
        embedding=OpenAIEmbeddings(),
        connection_args={
            "uri": ZILLIZ_CLOUD_URI,
            #"user": ZILLIZ_CLOUD_USERNAME,
            #"password": ZILLIZ_CLOUD_PASSWORD,
            "token": ZILLIZ_CLOUD_API_KEY,  # API key, for serverless clusters which can be used as replacements for user and password
            "secure": True,
        },
    )

    return

loadPdf("../doc/samsung_tooth_terms.pdf")
