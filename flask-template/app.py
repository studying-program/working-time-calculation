from flask import Flask, render_template, request
import re

app = Flask(__name__)

def parse_time(time_str):
    if not re.match(r'^\d{4}$', time_str):
        raise ValueError("Invalid time format")
    hours = int(time_str[:2])
    minutes = int(time_str[2:])
    return hours, minutes

@app.route('/', methods=['GET', 'POST'])
def index():
    total_time = None
    if request.method == 'POST':
        try:
            hours1, minutes1 = parse_time(request.form['time1'])
            hours2, minutes2 = parse_time(request.form['time2'])
            total_minutes = (hours1 * 60 + minutes1) + (hours2 * 60 + minutes2)
            total_hours = total_minutes // 60
            total_minutes = total_minutes % 60
            total_time = f"{total_hours:02}:{total_minutes:02}"
        except ValueError:
            total_time = "Invalid input. Please enter time in hhmm format."
    return render_template('index.html', total_time=total_time)

if __name__ == '__main__':
    app.run(debug=True)
