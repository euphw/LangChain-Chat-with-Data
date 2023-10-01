import os
import openai
import sys
sys.path.append('../..')

import constants

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("docs\LLXZ.pdf")
pages = loader.load()
len(pages)