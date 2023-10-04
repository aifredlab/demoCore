
from pymilvus import MilvusClient

ZILLIZ_CLOUD_URI = "https://in03-bfa4469b6404aa3.api.gcp-us-west1.zillizcloud.com"  # example: "https://in01-17f69c292d4a5sa.aws-us-west-2.vectordb.zillizcloud.com:19536"
ZILLIZ_CLOUD_USERNAME = ""  # example: "username"
ZILLIZ_CLOUD_PASSWORD = ""  # example: "*********"
ZILLIZ_CLOUD_API_KEY = "a3d25208a17af9679b40440b61aeee5c9ad11db43e49d21761f65c5034d2637dda67a4ddf1833bba3ea2c68900c2d169b34e2a8f"  # example: "*********" (for serverless clusters which can be used as replacements for user and password)

# Milvus 서버에 연결
client = MilvusClient(
            uri=ZILLIZ_CLOUD_URI,
            token=ZILLIZ_CLOUD_API_KEY
        )

# Milvus 서버에 연결
#client = Milvus(host='your_milvus_server_host', port='your_milvus_server_port')

# 스키마를 조회할 컬렉션 이름
collection_name = 'LangChainCollection'

# 컬렉션의 스키마 조회
status, schema = client.get_collection_stats(collection_name)

# 결과 확인 및 벡터 필드의 차원 출력
if status.OK():
    for field in schema.fields:
        # 벡터 필드의 차원 정보가 필요한 경우
        if field.type == DataType.VECTOR_FLOAT or field.type == DataType.VECTOR_BINARY:
            print(f"Vector field name: {field.name}, Dimension: {field.params['dim']}")
else:
    print("Error:", status)
