import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import Literal, Optional
from pydantic import BaseModel, Field

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OLLAMA_API_KEY")
   
model = ChatOpenAI(
    model="cogito-2.1:671b",
    openai_api_base="https://ollama.com/v1",
    max_completion_tokens=256,
    temperature=0
)

# Define the JSON Schema

user_review = """

I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking,
or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W 
fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, 
though I don't use it often. What really blew me away is the 200MP camera—the 
night mode is stunning, capturing crisp, vibrant images even in low light. 
Zooming up to 100x actually works well for distant objects,
but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. 
Also, Samsung’s One UI still comes with bloatware—why do I need five different 
Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

"""


response = model.invoke(user_review)

print(response.content)
print('-'*100)