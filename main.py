import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# CORS fix here 👇
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginRequest):
    if data.username == "satvik" and data.password == "1234":
        return {"message": "Login successful!"}
    return {"message": "Invalid credentials."}

# Ensure the app listens on the right port
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
