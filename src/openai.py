!pip install openai==0.28
!pip install python-dotenv
import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = "https://acc-alejandria-core-openaimagesound-pro.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

message_text = [{"role":"system","content":"Cuanto mide un oso polar?"}]

completion = openai.ChatCompletion.create(
  engine="gepeto",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion['choices'][0]['message'])