from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/api/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({"error": "No data"}), 400
        
        # Extrae el mensaje del aviso de TradingView
        mensaje = data.get("mensaje", "¡Alerta de Kemet! Algo pasó en el mercado. 🦁")
        if not mensaje:
            mensaje = str(data)
        
        # Configuración del bot y grupo de Telegram
        TELEGRAM_TOKEN = "7959634574:AAHSjTKvWLuakrAKxU4GQ4err6xOzasy59E"
        CHAT_ID = "-100096725017"  # Grupo PING
        
        # Envía el mensaje
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = {
            "chat_id": CHAT_ID,
            "text": mensaje,
            "parse_mode": "HTML"
        }
        response = requests.post(url, params=params)
        
        if response.status_code == 200:
            return jsonify({"ok": True, "mensaje_enviado": mensaje}), 200
        else:
            return jsonify({"error": f"Fallo en Telegram: {response.text}"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
