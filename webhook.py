import json

def handler(request, context):
    try:
        # Leer el cuerpo del request
        data = request.get_json()
        print("Mensaje recibido:", data)

        # Responder con éxito
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Webhook recibido correctamente"})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
