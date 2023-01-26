import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)







def __english_to_french__(english_text):

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    json.dumps(translation)
    list=translation['translations']
    french_text=list

    return french_text

def __french_to_english__(french_text):

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    json.dumps(translation)
    list=translation['translations'] 
    english_text=list 
    return english_text
