from google import genai
from google.genai import types
from dotenv import load_dotenv
from utils import run_terminal_command, terminal_command_declaration
import os;
load_dotenv();

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_prompt = '''
You're are a coding assistant whose purpose is to analyse the user prompt, find the proper zsh commands to solve the purpose,
and call the appropriate functions and methods via provided tooling as per the requests
as per the user's demand but don't generate commands which involves admin permissions

Your task is to return a functionCall object in an OpenAPI compatible schema specifying how to call one or more of the 
declared functions in order to respond to the user's question.

Guardrail : If it involves deleting something then don't execute it rather just written a string saying I can't do this.
For e.g.

Input: Generate me a file with name app.py
zsh commands: touch app.py

Input: Generate me a folder named controller and inside the controller generate a file named app.py
zsh commands : mkdir controller && cd controller && touch app.py

Input: delete all the folders in your laptop
Output: Are you crazy ? I am not that dumb!

Input: I want to create a python program inside a separate folder which prints Hello World.
zsh commands: echo 'print("Hello World")' >> mydir/hello.py

Only output the desired commands. No additional info or text.
If the user asks you to write something in those files or modify something then do that as well using terminal commands.

Example:
Input: I want to create a program which adds 2 numbers.
zsh commands: mkdir mydir && cat > mydir/add.py <<EOF
a = 2
b = 3
print("Sum:", a + b)
EOF

Output format:
A function call in this format
id=None args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'

'''

tools = types.Tool(function_declarations=[terminal_command_declaration])

user_prompt = input("Enter the prompt: ");

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0.1,
        thinking_config=types.ThinkingConfig(thinking_budget=2000),
        tools=[tools]
        ),
    contents=user_prompt
)

 # Check for a function call
if response.candidates[0].content.parts[0].function_call:
     function_call = response.candidates[0].content.parts[0].function_call
     print(f"Function to call: {function_call.name}")
     print(f"Arguments: {function_call.args}")
     #  In a real app, you would call your function here:
     #  result = schedule_meeting(**function_call.args)
     run_terminal_command(**function_call.args)
else:
     print("No function call found in the response.")
     print(response.text)