from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        print("Mensaje recibido:", data)
        return {"message": "Webhook recibido correctamente"}
    except Exception as e:
        print("Error:", str(e))
        return {"error": str(e)}

