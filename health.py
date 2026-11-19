
def calculate_health_score(battery_data):
    """
    Analyze battery health using actual capacity data.
    """

    if not battery_data.get("available"):
        return {
            "score": None,
            "condition": "Unavailable",
            "recommendation": "Battery information could not be accessed."
        }

    score = battery_data.get("health_score")

    if score is None:
        return {
            "score": None,
            "condition": "Unknown",
            "recommendation": "Battery capacity information is unavailable. Check battery report or hardware support."
        }

    if score >= 80:
        condition = "Good"
        recommendation = "Battery condition is good. Continue normal usage."
    elif score >= 60:
        condition = "Moderate"
        recommendation = "Battery capacity has reduced. Monitor battery performance."
    else:
        condition = "Poor"
        recommendation = "Battery capacity is low. Consider professional battery inspection."

    return {
        "score": score,
        "condition": condition,
        "recommendation": recommendation
    }
