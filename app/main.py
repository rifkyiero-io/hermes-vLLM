from fastapi import FastAPI

from app.providers.manager import ProviderManager

app = FastAPI()

provider = ProviderManager()


@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "Hermes AI",
    }


@app.get("/chat")
async def ask(q: str):

    answer = await provider.chat(
        [
            {
                "role": "user",
                "content": q,
            }
        ]
    )

    return {
        "question": q,
        "answer": answer,
    }
