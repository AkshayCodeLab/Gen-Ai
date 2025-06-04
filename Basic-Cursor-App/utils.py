import subprocess

def run_terminal_command(command: str):
    """
    Executes a terminal command and prints the output or error.
    
    Parameters:
        command (str): The terminal command to execute.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error occurred:")
        print(e.stderr)


terminal_command_declaration = {
    "name": "run_terminal_command",
    "description": "Execute the terminal command given the input string",
    "parameters": {
        "type": "object",
        "properties": {
            "command" : {
                "type": "string",
                "description" : "Input terminal command in the form of string"
            }
        },
        "required": ["command"],
    },
}
