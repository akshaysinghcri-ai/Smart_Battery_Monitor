
from flask import Flask, render_template, jsonify
from battery import get_battery_info
from health import calculate_health_score
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

DATA_FOLDER = "data"
LOG_FILE = os.path.join(DATA_FOLDER, "battery_log.csv")

os.makedirs(DATA_FOLDER, exist_ok=True)


def save_battery_data(data):
    if not data.get("available"):
        return

    record = {
        "timestamp": data["timestamp"],
        "percentage": data["percentage"],
        "charging_status": data["charging_status"],
        "health_score": data["health_score"]
    }

    df = pd.DataFrame([record])

    if os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(LOG_FILE, index=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/battery")
def battery_api():
    battery_data = get_battery_info()
    health_data = calculate_health_score(battery_data)

    if battery_data.get("available"):
        save_battery_data(battery_data)

    return jsonify({
        "battery": battery_data,
        "health": health_data
    })


if __name__ == "__main__":
    print("Smart Battery Monitoring System Started!")
    print("Open http://127.0.0.1:5000 in your browser")

    app.run(debug=True)
