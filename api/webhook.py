from fastapi import FastAPI, Request
import requests
import json

app = FastAPI()

TELEGRAM_TOKEN = "7959634574:AAHSjTKvWLuakAkXlJ4JQG4em6x0zasy5E"
CHAT_ID = "-100069725017"  # Grupo PING

@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        print("Mensaje recibido:", data)

        # Extraer el mensaje desde TradingView
        mensaje = data.get("mensaje", "⚡ Alerta de Kemet! Algo pasó en el mercado.")
        if not mensaje:
            mensaje = str(data)

        # Enviar mensaje a Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": mensaje,
            "parse_mode": "HTML"
        }

        response = requests.post(url, data=payload)
        print("Respuesta Telegram:", response.text)

        return {"status": "ok", "data": data}

    except Exception as e:
        print("Error:", str(e))
        return {"error": str(e)}

