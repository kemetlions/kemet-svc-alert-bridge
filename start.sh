#!/bin/bash
echo "Iniciando servidor Flask local..."
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=5000

