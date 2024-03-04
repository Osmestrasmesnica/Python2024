from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(debug=True)

#info ako hoces da otvoris html moras da ga stavis u folder template
#info takodje moras da importujes render_template metodu
#info ucitavanje static fajlova (slike, css) moras da ga stavis u foldera static