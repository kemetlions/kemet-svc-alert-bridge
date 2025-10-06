import json
import requests

def handler(event, context):
    try:
        # Lee el body del request (aviso de TradingView)
        data = json.loads(event['body'])
        
        if not data:
            return {'statusCode': 400, 'body': json.dumps({'error': 'No data'})}
        
        # Saca el mensaje del aviso
        mensaje = data.get('mensaje', '¡Alerta de Kemet! Algo pasó en el mercado. 🦁')
        
        # Si no hay 'mensaje', usa el texto completo
        if not mensaje:
            mensaje = str(data)
        
        # Tus secretos (ajustado para el grupo PING)
        TELEGRAM_TOKEN = "7959634574:AAHSjTKvWLuakrAKxU4GQ4err6xOzasy59E"
        CHAT_ID = "-100096725017"  # CHAT_ID del grupo PING
        
        # Manda el mensaje a Telegram (al grupo PING)
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = {
            'chat_id': CHAT_ID,
            'text': mensaje,
            'parse_mode': 'HTML'  # Para emojis y negritas
        }
        response = requests.post(url, params=params)
        
        if response.status_code == 200:
            return {'statusCode': 200, 'body': json.dumps({'ok': True, 'mensaje_enviado': mensaje})}
        else:
            return {'statusCode': 500, 'body': json.dumps({'error': 'Fallo en Telegram'})}
            
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
