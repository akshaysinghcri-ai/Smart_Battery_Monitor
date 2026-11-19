
import psutil
import subprocess
import re
from pathlib import Path
from datetime import datetime


def get_battery_capacity():
    report_path = Path(__file__).with_name("battery-report.html")

    try:
        subprocess.run(
            [
                "powercfg",
                "/batteryreport",
                "/output",
                str(report_path)
            ],
            capture_output=True,
            text=True,
            timeout=15
        )

        report = report_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        design = re.search(
            r"DESIGN\s+CAPACITY</span>\s*</td>\s*<td>\s*([\d,]+)\s*mWh",
            report,
            re.IGNORECASE
        )

        full = re.search(
            r"FULL\s+CHARGE\s+CAPACITY</span>\s*</td>\s*<td>\s*([\d,]+)\s*mWh",
            report,
            re.IGNORECASE
        )

        if design and full:
            return {
                "design_capacity": int(design.group(1).replace(",", "")),
                "full_capacity": int(full.group(1).replace(",", ""))
            }

    except Exception as error:
        print("Capacity error:", error)

    return {
        "design_capacity": None,
        "full_capacity": None
    }


def get_battery_info():
    battery = psutil.sensors_battery()

    if battery is None:
        return {
            "available": False,
            "message": "Battery information is not available."
        }

    capacity = get_battery_capacity()

    design = capacity["design_capacity"]
    full = capacity["full_capacity"]

    health = None

    if design and full and design > 0:
        health = min(round((full / design) * 100, 2), 100)

    if health is None:
        condition = "Unknown"
    elif health >= 80:
        condition = "Good"
    elif health >= 60:
        condition = "Moderate"
    else:
        condition = "Poor"

    return {
        "available": True,
        "percentage": round(battery.percent, 1),
        "plugged_in": battery.power_plugged,
        "charging_status": (
            "Charging" if battery.power_plugged else "Discharging"
        ),
        "design_capacity": design,
        "full_charge_capacity": full,
        "health_score": health,
        "condition": condition,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
