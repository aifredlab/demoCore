import os
#@markdown https://platform.openai.com/account/api-keys
OPENAI_API_KEY = "" #@param {type:"string"}

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
    from opengpt import classfication as cf
    #import opengpt from classfication as gen
    #import opengpt from classfication as 
else:
    print("후추 구현")


print(cf.main("약관 조회"))
