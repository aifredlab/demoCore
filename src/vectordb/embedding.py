
import openai
import os

def embedding_openai(text):
    return openai.Embedding.create(
        input=text, 
        engine=os.environ.get('OPENAI_ENGINE'))["data"][0]["embedding"]


#print ( embedding_openai("aaa") )

