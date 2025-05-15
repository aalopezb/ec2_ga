from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Microservicio de consulta a PokeAPI
@app.route("/pokemon")
def obtener_pokemon():
    nombre = request.args.get("nombre")
    if not nombre:
        return jsonify({"error": "No se proporcionó el nombre"}), 400

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Pokémon no encontrado"}), 404

    data = response.json()
    return jsonify({
        "nombre": data["name"],
        "altura": data["height"],
        "peso": data["weight"],
        "imagen": data["sprites"]["front_default"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
