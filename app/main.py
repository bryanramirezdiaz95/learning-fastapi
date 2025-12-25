from fastapi import FastAPI

app = FastAPI()
app.title = "API title"

@app.get("/")
async def hello_world():
    return {"message": "Hello World!"}