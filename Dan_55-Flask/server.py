from flask import Flask
import random

random_broj = random.randint(0,9)
print(random_broj)

app = Flask(__name__) # ovo name znaci da se module pokrece iz ovog fajla i nije importovano

@app.route("/") # ovo znaci ako se ukuca url i na kraju / onda treba homepage da se otvori
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnFybHZiY3F3Zzd4eWFrNXV2bXk4OG1kZHBzdjQ0bTRpbWxxaHg0cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif' width=450 />"

@app.route("/<int:guess>")
def guess_random_number(guess):
    if int(guess) == random_broj:
        return "<h1>You guessed the number!</h1>"\
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=450 />"
    elif int(guess) > random_broj:
        return "<h1>Too high, try again!!</h1>"\
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=450 />"
    elif int(guess) < random_broj:
        return "<h1>Too low, try again!!</h1>"\
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=450 />"

if __name__ == "__main__":
    app.run(debug=True)