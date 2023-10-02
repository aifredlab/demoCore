import os
import json

#@markdown https://platform.openai.com/account/api-keys
OPENAI_API_KEY = "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" #@param {type:"string"}

#@markdown https://huggingface.co/settings/tokens
#@markdown HuggingFace에서 모델 다운로드나 클라우드 모델 사용하기 위해서 필요 (무료)
HUGGINGFACEHUB_API_TOKEN = "" #@param {type:"string"}

#@markdown https://serpapi.com/manage-api-key
#@markdown 구글 검색하기 위해서 필요 (월 100회 무료)
SERPAPI_API_KEY = "" #@param {type:"string"}

MODEL_NAME = "GPT" #@param {type:"string"}

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY

if MODEL_NAME == "GPT":
    from opengpt import classfication as cf     # 카테고리 리턴
    from vectordb import similarity as sm       # Document 리턴
    from opengpt import combine_documents_stuff as cd       # chat 리턴
    
else:
    print("후추 구현")

##################################################
class Aifred:
    def __init__(self, value):
        self.prompt = value

    def process(self):
        prompt = self.prompt
        result = "test"

        cfResult = cf.main(prompt);
        print(f"cfResult {cfResult}")

        category = cfResult["category"]

        if category == "보험료계산":
            print("보험료계산로직.......")
        elif category == "약관조회":
            print("약관조회로직.......")
            smReulst = sm.main(prompt)
            print(f"smReulst {smReulst}")
        else:
            print("ERRORERRORERRORERRORERRORERROR")
    
        return result;

if __name__ == "__main__":
    #process()
    aifred_instance = Aifred("보험료계산을 해주세요")  # Aifred 클래스의 인스턴스 생성
    aifred_instance.process()  # process 메서드 호출
    



