from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

filename = "dictionary.csv"
df = pd.read_csv(filename)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/api/t1/<word>/")
def about(word):
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    return {"word": word,
            "definition": definition
            }


if __name__ == "__main__":
    app.run(debug=True, port=5001)
