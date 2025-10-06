from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Tus secretos (¡no cambies esto!)
TELEGRAM_TOKEN = "7959634574:AAHSjTKvWLuakrAKxU4GQ4err6xOzasy59E"
CHAT_ID = "5870967116"

@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.get_json()  # Escucha el aviso de TradingView
        if not data:
            return jsonify({'error': 'No data'}), 400
        
        # Saca el mensaje del aviso (TradingView lo manda en JSON)
        mensaje = data.get('mensaje', '¡Alerta de Kemet! Algo pasó en el mercado. 🦁')
        
        # Si no hay 'mensaje', usa el texto completo como fallback
        if not mensaje:
            mensaje = str(data)
        
        # Manda el mensaje a tu bot en Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = {
            'chat_id': CHAT_ID,
            'text': mensaje,
            'parse_mode': 'HTML'  # Para que llegue bonito con emojis
        }
        response = requests.post(url, params=params)
        
        if response.status_code == 200:
            return jsonify({'ok': True, 'mensaje_enviado': mensaje})
        else:
            return jsonify({'error': 'Fallo en Telegram'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500
