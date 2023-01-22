import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3
version ='{version}',
authenticator = authenticator
language_translator.set_service_url('{url}')

def englishToFrench(englishText):
    
    for text in englishText:
       
        frenchText = language_translator.translate(text:[englishText], modelid='en-fr')
    
     return frenchText

def frenchToEnglish(frenchText):
    
    for text in frenchText:
        
        englishText = language_translator.translate(text: [frenchText], modelid= 'fr-en')
    
    return englishText