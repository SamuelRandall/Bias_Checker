# -----------------------------------------
# main.py
# creating first flask application
# -----------------------------------------

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Bias checker"


if __name__ == "__main__":
    app.run(debug=True)
# ----------------------------------------
# end of main.py
# ----------------------------------------
