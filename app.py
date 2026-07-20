from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from route_service import get_routes
from weather import get_weather
from ai import analyze_routes
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/build-route", methods=["POST"])
def build_route():

    data = request.get_json()

    start = data.get("start")
    destination = data.get("destination")

    if not start or not destination:
        return jsonify({
            "error": "Start and destination are required."
        }), 400

    # ==========================
    # Get routes
    # ==========================

    routes = get_routes(start, destination)

    if not routes:
        return jsonify({
            "error": "Unable to build route."
        }), 400

    # ==========================
    # Weather
    # ==========================

    try:
        lat, lon = map(float, destination.split(","))

        weather = get_weather(lat, lon)

    except Exception:

        weather = {
            "temperature": "Unknown",
            "condition": "Unknown",
            "description": "Unknown",
            "wind": 0
        }

    # ==========================
    # AI Recommendation
    # ==========================

    try:
        ai_response = analyze_routes(
            routes,
            weather
        )

    except Exception as e:

        ai_response = f"AI is temporarily unavailable.\n\n{e}"

    # ==========================
    # Response
    # ==========================

    return jsonify({

        "success": True,

        "weather": weather,

        "routes": routes,

        "ai": ai_response

    })


@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "success": False,
        "error": "Page not found."
    }), 404


@app.errorhandler(500)
def server_error(error):

    return jsonify({
        "success": False,
        "error": "Internal server error."
    }), 500


import os

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        debug=False,
        host="0.0.0.0",
        port=port
    )
