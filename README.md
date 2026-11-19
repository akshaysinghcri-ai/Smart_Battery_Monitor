# Smart Battery Health & Usage Monitoring System

## Project Overview
The Smart Battery Health & Usage Monitoring System is a Python-based web application developed using Flask. It monitors laptop battery information, estimates battery health, displays charging status, and records battery usage data.

The system provides a simple and user-friendly dashboard to understand battery performance and condition.

## Objectives
- To monitor laptop battery percentage in real time.
- To display battery charging status.
- To estimate battery health using design capacity and full charge capacity.
- To maintain a record of battery usage.
- To provide battery condition information and recommendations.

## Key Features
- Live battery percentage monitoring.
- Charging and power connection status.
- Battery health score calculation.
- Battery condition classification: Good, Moderate, and Poor.
- Display of design capacity and full charge capacity.
- Automatic battery data logging in CSV format.
- User-friendly web dashboard.
- Automatic dashboard refresh.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- Pandas
- Psutil
- Windows Battery Report

## Project Structure
```text
Smart_Battery_Monitor/
├── app.py
├── battery.py
├── health.py
├── requirements.txt
├── data/
│   └── battery_log.csv
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    └── index.html
```

## System Working
1. The system retrieves battery information using Python.
2. Battery capacity details are collected from the Windows battery report.
3. Battery health is estimated using design capacity and full charge capacity.
4. Flask provides battery information through a web application.
5. The dashboard displays battery details.
6. Battery readings are stored in a CSV file.

## Battery Health Calculation

Battery Health (%) = (Full Charge Capacity / Design Capacity) × 100

The calculated score is capped at 100%.

## Installation and Execution

1. Install Python on your Windows system.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python app.py
```

6. Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

## Testing and Validation
- Battery percentage monitoring.
- Battery capacity information verification.
- Battery health score calculation.
- Charging status display.
- CSV data logging.
- Dashboard functionality testing.

## Expected Outcome
A simple and user-friendly Battery Health Monitoring System that displays available battery information, estimates battery condition, and maintains battery usage records in a single dashboard.

## Future Scope
- Battery usage graphs and analytics.
- Historical battery performance comparison.
- Improved battery discharge analysis.
- Notifications for low battery health.

## Author
**Akshay Singh Chaudhary**

## GitHub Repository
https://github.com/akshaysinghcri-ai/Smart_Battery_Monitor
