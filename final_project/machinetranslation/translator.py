"""
Provides translation from english to french and french to english
"""

import json

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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


def englishToFrench(englishText):
    """Translate from english to french"""
    if englishText == "" or englishText is None:
        return "You need to send an input"

    french_text = language_translator.translate(
    englishText,
    model_id='en-fr').get_result()
    print(json.dumps(french_text, indent=2, ensure_ascii=False))

    return french_text["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    """Translate from french to english"""
    if frenchText == "" or frenchText is None:
        return "You need to send an input"

    english_text = language_translator.translate(
    frenchText,
    model_id='fr-en').get_result()
    print(json.dumps(english_text, indent=2, ensure_ascii=False))

    return english_text["translations"][0]["translation"]
