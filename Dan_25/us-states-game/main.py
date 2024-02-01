 #! US States Game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
screen.setup(width = 725, height = 495)
image = "Dan_25/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Funckija koja printujhe x i y koordinatu kada stisnemo misem
# def get_mouse_click_coor(x,y):
#     print(x,y)

# # Kada kliknemo dobijemo x i y koordinatu gde smo kliknuli
# turtle.onscreenclick(get_mouse_click_coor)


data = pandas.read_csv("Dan_25/us-states-game/50_states.csv")
all_states = data.state.to_list()
broj_pogodaka = []
print(all_states)

# dok je broj pogodaka manji od ukupnog broja igramo igru
while len(broj_pogodaka) < len(all_states):

    # input unosimo
    answer_state = screen.textinput(title=f"{len(broj_pogodaka)}/50 drzava u Americi", prompt="Upišite naziv zemlje (onako kako se piše na engleskom)").title()
    
    # ako je u input Exit, izlazimo iz loopa
    if answer_state == "Exit":
        missing_states = []
        for state in all_states: # --> za svaku drzavu u list svih drzava
            if state not in broj_pogodaka: # --> ako nema drzave u listi pogodaka
                missing_states.append(state) # --> dodajemo u novu listu
        new_data = pandas.DataFrame(missing_states) # --> pravimo od nove liste nov csv sa spiskom onih drzava koje nismo pogodili
        new_data.to_csv("Dan_25/us-states-game/states_to_learn.csv")
        break # --> izlazimo iz while loopa da bi videli lepo mapu
    
    # Provera da nisi vec istu drzavu
    if answer_state in broj_pogodaka:
        print("You've already guessed that one!")

    #! ovo "IN" moze samo ako smo prethodno data prebacili u to_list()!!!!!  
    elif answer_state in all_states: # --> ako je input koji smo uneli u okviru spiska svih drzava
        broj_pogodaka.append(answer_state) # --> dodajemo tu drzavu u nasu listu sa pogodjenim drzavama
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y)) #! --> konvertovati u integer, saljemo turtle na poziciju x i y od "state" koji smo pogodili
        t.write(answer_state) #? nisam znao da write moze i bez ostalih parametra kao sto su font i alignment


# Sprecava da se izadje na klik misem
turtle.mainloop()

