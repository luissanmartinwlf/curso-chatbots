from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
apikey = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=apikey)

response = client.responses.create(
    model="gpt-4o-mini",  
    input ="Cuntame un chiste sobre elefantes"
)   
print(response.output_text)