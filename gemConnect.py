from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import dataLoad 
import time


load_dotenv()

class QuestAnsw(BaseModel):
    question: str
    answer: str    

_context_cache = None

class agent():
    def get_context(self,module): #Cache loadAll, so that each agent call does not have not process files again
        global _context_cache
        if _context_cache is None:
            ld = dataLoad.dataLoad()
            _context_cache = ld.loadAll(module)
            print("-----Context succesfully cached...-----")
        return _context_cache

    def query(self,prp, module):
        start_time = time.time()
        context = self.get_context(module)
        client = genai.Client(api_key=os.getenv('GEMINI_API'))
        if prp is not None:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Using the context:\n{context} answer the users prompt: {prp}. Use the user prompt as 'question'",
                config={
                    "response_mime_type": "application/json",
                    "response_schema": list[QuestAnsw],
                },
            )
            output: list[QuestAnsw] = response.parsed
            dict_list = [m.model_dump() for m in output]
            print("Succesfully prompted and recieved a response...")
            return dict_list
        else:
            print("No input and/or context given")
            
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Prompting and recieving answer: {round(elapsed_time,3)} seconds...")
