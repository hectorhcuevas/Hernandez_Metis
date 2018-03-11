# minimal example from:
# http://flask.pocoo.org/docs/quickstart/

import json

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    #df = pd.read_csv('data').drop('Open', axis=1)
    chart_data = data.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("game_of_life.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
# runs as default if you $python app.py, instead of a module: http://thepythonguru.com/what-is-if-__name__-__main__/
@app.route("/")
    return render_template("game_of_life.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)

