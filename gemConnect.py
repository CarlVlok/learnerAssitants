from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import dataLoad 


load_dotenv()

class QuestAnsw(BaseModel):
    question: str
    answer: str    

_context_cache = None

def get_context(): #Cache loadAll, so that each agent call does not have not process files again
    global _context_cache
    if _context_cache is None:
        ld = dataLoad.dataLoad()
        _context_cache = ld.loadAll()
    return _context_cache

def agent(prp):
    context = get_context()
    client = genai.Client(api_key=os.getenv('GEMINI_API'))
    if prp != None:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Using the content from {context}, return the prompt given by the user {prp} and the answer",
            config={
                "response_mime_type": "application/json",
                "response_schema": list[QuestAnsw],
            },
        )

        return response.text
    else:
        print("No input and/or context given")



#output: list[QuestAnsw] = response.parsed
