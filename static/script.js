
async function updateBattery() {
    try {
        const response = await fetch("/api/battery");
        const result = await response.json();

        const battery = result.battery;
        const health = result.health;

        if (!battery.available) {
            document.getElementById("recommendation").textContent =
                battery.message;
            return;
        }

        document.getElementById("percentage").textContent =
            battery.percentage + "%";

        document.getElementById("batteryBar").style.width =
            battery.percentage + "%";

        document.getElementById("charging").textContent =
            battery.charging_status;

        document.getElementById("healthScore").textContent =
            health.score === null ? "N/A" : health.score + "%";

        document.getElementById("condition").textContent =
            health.condition;

        document.getElementById("batteryCondition").textContent =
            health.condition;

        document.getElementById("designCapacity").textContent =
            battery.design_capacity
                ? battery.design_capacity + " mWh"
                : "Not available";

        document.getElementById("fullCapacity").textContent =
            battery.full_charge_capacity
                ? battery.full_charge_capacity + " mWh"
                : "Not available";

        document.getElementById("updated").textContent =
            battery.timestamp;

        document.getElementById("recommendation").textContent =
            health.recommendation;

    } catch (error) {
        document.getElementById("recommendation").textContent =
            "Unable to connect to the battery monitoring server.";
    }
}

updateBattery();
setInterval(updateBattery, 5000);
