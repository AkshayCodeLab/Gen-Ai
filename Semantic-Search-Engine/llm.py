from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model

def get_answer(context, user_query):
    
    template = ChatPromptTemplate([
        ("system", "Based on this context : {context},  Answer the following user query. Don't give too large or too short explanations. Give to the point answers."),
        ("human", "{query}")
    ])
    
    prompt_value = template.invoke({
        "context" : context,
        "query" : user_query
    })
    
    model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
    
    response = model.invoke(prompt_value)
    print(response.content)
    
    
        
    

    
    
    
    