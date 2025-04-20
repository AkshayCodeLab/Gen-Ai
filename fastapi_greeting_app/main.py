from fastapi import FastAPI
import random

app = FastAPI()

greetings = [
    "Hello, World!",
    "Greetings!",
    "Hi there!",
    "Welcome!",
    "Hey!",
]

@app.get("/")
async def read_root():
    return {"message": random.choice(greetings)}
EOF && echo "fastapi
uvicorn" > requirements.txt
