import os
import json
from dotenv import load_dotenv

MODEL_NAME="GPT"

if MODEL_NAME == "GPT":
    from opengpt import classfication as cf     # 카테고리 리턴
    from vectordb import similarity as sm       # Document 리턴
#    from opengpt import combine_documents_stuff as cd       # chat 리턴
    from opengpt import chat as cd              # 카테고리 리턴
else:
    print("후추 구현")


##################################################
class Aifred:
    def __init__(self):
        # 환경변수 로드 (.env 파일 로드)
        load_dotenv()

    def process(self, prompt):
        result = "empty"

        cfResult = cf.main(prompt);
        print(f"cfResult {cfResult}")

        category = cfResult["category"]

        # 약관용으로 데모버전을 만들어서 하드코딩함
        category = "약관조회"

        if category == "보험료계산":
            print("보험료계산로직.......")
            result = category
        elif category == "약관조회":
            print("약관조회로직.......")

            # 약관 조회 
            smResult = sm.search(prompt)
            
            # LLM 호출
            cdResult = cd.main(smResult, prompt)
            result = cdResult
        else:
            print("ERRORERRORERRORERRORERRORERROR")
    
        return result;

if __name__ == "__main__":
    aifred_instance = Aifred()  # Aifred 클래스의 인스턴스 생성
    aifred_instance.process("이 상품을 가입해서 만기가 되면 보험료 전액 환급이 가능해?")  # process 메서드 호출
    

