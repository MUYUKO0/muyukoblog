# Muyuko web page - Flask app

from flask import Flask, render_template

app = Flask(__name__)

konu = ["Minecraft", "Youtube", "Python", "Java"]  # örnek


@app.route("/")
def main():
    return render_template("index.html", konu=konu)


if __name__ == "__main__":
    app.run(debug=True)
