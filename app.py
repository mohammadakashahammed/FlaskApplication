import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)

