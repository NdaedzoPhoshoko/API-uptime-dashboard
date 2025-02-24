'''
Packages:
python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install Flask
    pip install requests
'''
from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)
start_time = datetime.now()

@app.route('/')
def home():
    return render_template('index.html')

# API Endpoint for Uptime
@app.route('/api/uptime', methods=['GET'])
def get_uptime():
    uptime_seconds = (datetime.now() - start_time).total_seconds()
    uptime_minutes = int(uptime_seconds // 60)
    progress_percentage = min((uptime_minutes / 1440) * 100, 100)  # Adjust to fit within 100% over a day
    return jsonify(minutes_online=uptime_minutes, progress=str(int(progress_percentage*100))+ "%")

if __name__ == '__main__':
    app.run(debug=True)
