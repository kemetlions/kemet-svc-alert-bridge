from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import requests

class handler(BaseHTTPRequestHandler):

    # Tus secretos (¡no cambies esto!)
    TELEGRAM_TOKEN = "7959634574:AAHSjTKvWLuakrAKxU4GQ4err6xOzasy59E"
    CHAT_ID = "5870967116"

    def do_POST(self):
        try:
            # Lee el cuerpo del request (aviso de TradingView)
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)  # Parsea el JSON
            
            if not data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No data'}).encode('utf-8'))
                return
            
            # Saca el mensaje del aviso
            mensaje = data.get('mensaje', '¡Alerta de Kemet! Algo pasó en el mercado. 🦁')
            
            # Si no hay 'mensaje', usa el texto completo
            if not mensaje:
                mensaje = str(data)
            
            # Manda el mensaje a Telegram
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            params = {
                'chat_id': CHAT_ID,
                'text': mensaje,
                'parse_mode': 'HTML'  # Para emojis y negritas
            }
            response = requests.post(url, params=params)
            
            if response.status_code == 200:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'ok': True, 'mensaje_enviado': mensaje}).encode('utf-8'))
            else:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Fallo en Telegram'}).encode('utf-8'))
                
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
