from flask import Flask, render_template, send_file
import threading
import time
import psutil  # For local testing of resource constraints (can be replaced with Kubernetes API queries)

app = Flask(__name__)

# Serve the Kepler.gl HTML file
@app.route('/')
def index():
    return send_file('melt_kepler.gl.html')  # Replace with the path to your HTML file

# API to trigger animations
@app.route('/trigger-animation', methods=['POST'])
def trigger_animation():
    return {'status': 'Animation triggered'}

def monitor_resources():
    while True:
        # Simulate resource constraint monitoring
        disk_usage = psutil.disk_usage('/').percent
        if disk_usage > 80:  # Example: trigger animation if disk usage > 80%
            print("High disk usage detected! Triggering animation...")
            # You can integrate WebSocket here to send this data to the front end
        time.sleep(5)

# Start resource monitoring in a separate thread
threading.Thread(target=monitor_resources, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
