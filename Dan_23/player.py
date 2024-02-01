from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("dark green")
        self.reset()

    # funkcija za pokretanje kada se stisne dugme w ili strelica na gore
    def move(self):
        """Move turtle up"""
        #! ovo si ga ti iskomplikovao kako da se krece
        # new_y = self.ycor() + 10
        # self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)
    
    # funkcija za detektovanje da li smo prosli ulicu, ako jesmo onda resetujemo poziciju kornjace
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # funkcija za restartovanje pozicije kada se pređe cilj
    def reset(self):
        """Reset turtle position"""    
        self.goto(STARTING_POSITION)