import openai
import os
from time import sleep
from deep_translator import deepl
from json import loads

openai.api_key = os.environ.get("TOKEN_OPENAI")
OpenAI = openai.Completion

no_answer = "Je ne peux pas vraiment te répondre à ça..."

deep_l_token = os.environ.get("TOKEN_DEEPL")

translatorFR_EN = deepl.DeeplTranslator(api_key = deep_l_token, source = "fr", target = "en")
translatorEN_FR = deepl.DeeplTranslator(api_key = deep_l_token, source = "en", target = "fr")

def getEng(text) :
    try:
        return translatorFR_EN.translate(str(text))
    except:
        return text
def getFra(text) :
    try:
        return translatorEN_FR.translate(str(text))
    except:
        return text
def correctly(text: str) :
    sentences = text.split("\n")
    for i in range(len(sentences)) : sentences[i] = sentences[i].strip().replace("\n", "")
    lengths = tuple(map(lambda s: len(s), sentences))
    max_length = max(lengths)
    result = no_answer
    index = -1
    for i in range(len(lengths)) :
        length = lengths[i]
        if length == max_length :
            index = i
    if index != -1 :
        result = sentences[index]
    return result

def analyse(result) :
    data = dict(loads(str(result)))
    choices = data["choices"]
    if choices is not None :
        text = choices[0]["text"]
        if len(text) != 0 :
            return correctly(text)
        else : return no_answer
    else : return no_answer

def ask(message: str) :
    message = getEng(message.strip())
    response = OpenAI.create(model= "text-davinci-002", prompt= message, temperature=0, max_tokens=60, top_p= 1, best_of=1)
    response = analyse(response)
    response = getFra(response)
    return response
