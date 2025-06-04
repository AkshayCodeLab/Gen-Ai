from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from variable_extractor import variable_extractor

load_dotenv()

output = variable_extractor("I want to find out how people welcome each other when someone new enters the town in hindi")
print(output)
# model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# messages = [
#     SystemMessage("Do as it's asked"),
#     HumanMessage("I want to see how we greet people at the time of festivals in spanish")
# ]

# for token in model.stream(messages):
#     print(token.content, end="|")

