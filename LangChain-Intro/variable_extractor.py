from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
import json
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

system_prompt = """

You're a template variable extractor. Your task is to extract the template variables from the user's input and output them in JSON format.

variables to be extracted:
1. Language : specifies the language to which the sentence has to be converted.
2. content : Specifies the content which is to be translated.

Return a JSON output like :
{
    "language" : {...},
    "content" : {...}
}
don't return a string of json. just return json output.
"""

def variable_extractor(user_prompt):
    messages = [
        SystemMessage(system_prompt),
        HumanMessage(user_prompt)
    ]
    
    output = model.invoke(messages)
    try:
        return json.loads(output.content)  # ensures it's parsed to a Python dict
    except json.JSONDecodeError:
        print("Warning: JSON parsing failed. Raw output:")
        print(output.content)
        return None