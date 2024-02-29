from flask import Flask
app = Flask(__name__) # ovo name znaci da se module pokrece iz ovog fajla i nije importovano

@app.route("/") # ovo znaci ako se ukuca url i na kraju / onda treba homepage da se otvori
def hello_world():
    return "Hello World!"

@app.route("/anka")
def anka():
    return f"Leka voli Anku.... SCE SCAAAA STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOooooooooooooooOoo"

# Da ne moramo u konzolu da pisemo Fask main.py i ostale stvari mozemo samo ovo ispod da ubacimo
if __name__ == "__main__": 
    app.run()