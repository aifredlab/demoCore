
import openai

OPENAI_ENGINE = "text-embedding-ada-002" 
openai.api_key = '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'

def embedding_openai(text):
    return openai.Embedding.create(
        input=text, 
        engine=OPENAI_ENGINE)["data"][0]["embedding"]


#print ( embedding_openai("aaa") )

