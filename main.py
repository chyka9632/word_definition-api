from flask import Flask as fl, render_template
import pandas as pd

app = fl(__name__)
df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df["word"] == word]["definition"].squeeze()
    word = word.upper()
    result_dictionary = {"word": word, "definition": definition}
    return result_dictionary


app.run(debug=True, port=5001)
