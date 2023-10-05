
from pymilvus import MilvusClient
import os


# Milvus 서버에 연결
client = MilvusClient(
            uri=os.environ.get('ZILLIZ_CLOUD_URI'),
            token=os.environ.get('ZILLIZ_CLOUD_API_KEY')
        )

# Milvus 서버에 연결
#client = Milvus(host='your_milvus_server_host', port='your_milvus_server_port')

# 스키마를 조회할 컬렉션 이름
collection_name = os.environ.get('COLLECTION_NAME')

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
