
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

# Az alkalmazás létrehozása
app = Flask(__name__)
CORS(app)  # Engedélyezi az összes külső eredetű kérést

# Válaszok generálására szolgáló függvény meghatározása
def chatbot_response(message):
    # Felhasználói bemenet alapján válaszüzenet meghatározása
    if message == "init":
        response = "Üdvözöljük a Lora AI chatbot funkció teszjében."
    elif message == "Nyitvatartás":
        response = "Az üzletünk hétköznapokon 8 és 18 óra között van nyitva."
    elif message == "Termékinformáció":
        response = "A termék árát és a raktáron lévő mennyiséget megtalálja a weboldalunkon."
    elif message == "Rendelés":
        response = "A rendeléseket a weboldalon keresztül lehet leadni."
    else:
        response = "Sajnáljuk, de a kérdésére nem tudunk válaszolni."

    return response

# Beérkező üzenetek kezelésére szolgáló függvény meghatározása
@app.route('/message', methods=['POST'])
def handle_message():
    # Üzenet lekérése a kéréstől
    message = request.get_json()['message']

    # Válasz generálása
    response = chatbot_response(message)

    # Válasz JSON formátumba alakítása és visszaadása
    response = {'message': response}
    return jsonify(response)

# HTML oldal megjelenítésére szolgáló függvény meghatározása
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
