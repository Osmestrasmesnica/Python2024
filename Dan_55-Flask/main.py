from flask import Flask
app = Flask(__name__) # ovo name znaci da se module pokrece iz ovog fajla i nije importovano

@app.route("/") # ovo znaci ako se ukuca url i na kraju / onda treba homepage da se otvori
def hello_world():
    return "Hello World!"

@app.route("/anka")
def anka():
    return f"Leka voli Anku.... SCE SCAAAA STOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOooooooooooooooOoo"


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route("/bye")
@make_bold
@make_underline
@make_emphasis
def bye():
    return "Bye"

# Da ne moramo u konzolu da pisemo Fask main.py i ostale stvari mozemo samo ovo ispod da ubacimo
if __name__ == "__main__": 
    app.run(debug=True) # Aktiviramo debuger da moze da se autmoatski refreshuje server kada usnimimo u kocu, takodje mozemo da debagujemo live kod koristeci CODE koji smo dobili za ovaj server

