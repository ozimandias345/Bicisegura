from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# 📍 Lista temporal de puntos (luego puede ser BD)
puntos_ruta = []

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta del mapa
@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

# --- Guardar Punto ---
@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    data = request.get_json()

    lat = data.get('lat')
    lng = data.get('lng')

    if lat is None or lng is None:
        return jsonify({"status": "error", "message": "Datos inválidos"}), 400

    punto = {
        "lat": lat,
        "lng": lng
    }

    puntos_ruta.append(punto)

    print(f"📍 Punto agregado: {punto}")
    print(f"🛣️ Ruta actual: {puntos_ruta}")

    time.sleep(0.3)

    return jsonify({
        "status": "ok",
        "message": "Punto guardado",
        "total_puntos": len(puntos_ruta)
    })

# --- Obtener Ruta Completa ---
@app.route('/obtener_ruta', methods=['GET'])
def obtener_ruta():
    return jsonify({
        "status": "ok",
        "ruta": puntos_ruta
    })

# --- Limpiar Ruta ---
@app.route('/limpiar_ruta', methods=['POST'])
def limpiar_ruta():
    puntos_ruta.clear()
    return jsonify({
        "status": "ok",
        "message": "Ruta limpiada"
    })

if __name__ == '__main__':
    app.run(debug=True)
