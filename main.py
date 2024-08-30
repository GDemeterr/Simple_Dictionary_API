from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/api/t1/<word>/")
def about(word):
    definition = word.upper()
    return {"definition": definition,
            "word": word
            }


if __name__ == "__main__":
    app.run(debug=True, port=5001)