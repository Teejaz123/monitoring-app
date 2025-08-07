import psutil
from flask import Flask, render_template

app = Flask(__name__)

# Thresholds for alerting
CPU_ALERT_THRESHOLD = 80
MEMORY_ALERT_THRESHOLD = 80

@app.route("/")
def index():
    # Get CPU and Memory usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    # Alert message if thresholds are exceeded
    message = None
    if cpu_usage > CPU_ALERT_THRESHOLD or memory_usage > MEMORY_ALERT_THRESHOLD:
        message = "⚠️ High CPU or Memory usage detected. Consider scaling up!"

    return render_template(
        "index.html",
        cpu_metric=cpu_usage,
        mem_metric=memory_usage,
        message=message
    )

if __name__ == "__main__":
    # Run the Flask app on all interfaces (useful for Docker or VM)
    app.run(debug=True, host="0.0.0.0")
