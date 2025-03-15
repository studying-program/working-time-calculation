from flask import Flask, render_template, request
import re

app = Flask(__name__)

def parse_time(time_str):
    match = re.match(r'^(\d{1,2}):(\d{2})$', time_str)
    if not match:
        raise ValueError("Invalid time format")
    hours, minutes = map(int, match.groups())
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
            total_time = "Invalid input. Please enter time in hh:mm format."
    return render_template('index.html', total_time=total_time)

if __name__ == '__main__':
    app.run(debug=True)
