import os
import json
from dotenv import load_dotenv


MODEL_NAME="GPT"

if MODEL_NAME == "GPT":
    from opengpt import classfication as cf     # 카테고리 리턴
    from vectordb import similarity as sm       # Document 리턴
    from opengpt import combine_documents_stuff as cd       # chat 리턴
    
else:
    print("후추 구현")


##################################################
class Aifred:
    def __init__(self):
        # 환경변수 로드 (.env 파일 로드)
        load_dotenv()
        # print (os.environ.get('DATABASE_URL'))


    def process(self, prompt):
        result = "test"

        cfResult = cf.main(prompt);
        print(f"cfResult {cfResult}")

        category = cfResult["category"]

        if category == "보험료계산":
            print("보험료계산로직.......")
        elif category == "약관조회":
            print("약관조회로직.......")
            smReulst = sm.search(prompt)
            print(f"smReulst {smReulst}")
        else:
            print("ERRORERRORERRORERRORERRORERROR")
    
        return result;

if __name__ == "__main__":
    aifred_instance = Aifred()  # Aifred 클래스의 인스턴스 생성
    aifred_instance.process("약관조회 해약환급금 에 관한 사항")  # process 메서드 호출
    

