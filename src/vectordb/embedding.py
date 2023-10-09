
import openai
import os

def embedding_openai(text):

    openai.api_key = os.environ.get('OPENAI_API_KEY')
    return openai.Embedding.create(
        input=text, 
        engine=os.environ.get('OPENAI_ENGINE'))["data"][0]["embedding"]


#print ( embedding_openai("aaa") )

