from pymilvus import MilvusClient
import embedding as embedding       # Document 리턴

# replace
ZILLIZ_CLOUD_URI = "https://in03-bfa4469b6404aa3.api.gcp-us-west1.zillizcloud.com"
ZILLIZ_CLOUD_USERNAME = ""
ZILLIZ_CLOUD_PASSWORD = ""
ZILLIZ_CLOUD_API_KEY = "a3d25208a17af9679b40440b61aeee5c9ad11db43e49d21761f65c5034d2637dda67a4ddf1833bba3ea2c68900c2d169b34e2a8f" 
COLLECTION_NAME = "LangChainCollection"

def search(prompt):
    client = MilvusClient(
        uri=ZILLIZ_CLOUD_URI,
        token=ZILLIZ_CLOUD_API_KEY, # for serverless clusters, or
    )

    vector_data = embedding.embedding_openai(prompt)
    #print(f"##################={len(vector_data)}")

    res = client.search(
        collection_name=COLLECTION_NAME,
        data=[ vector_data ],
        limit=5,
        output_fields=["text"]
    )
    print(f"# collection search = {res}")
    print("------------------------------------------\n\n")
    
    return res;

# test
# print(  search("계약자가  회사에  보험수익자가  변경되었음을  통지하기  전에") )

